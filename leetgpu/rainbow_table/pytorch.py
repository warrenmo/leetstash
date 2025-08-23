"""
Below are 4 versions for solving the problem.
    - V1 solves the problem in what is most likely the expected way:
      copy the `input` into the `output` and then repeatedly apply the hash to
      `output`
    - V2 moves the type cast to torch.int64 out of the for-loop by allocating a
      `tmp` tensor in the beginning of the function of type torch.int64
    - V3 uses bit arithmetic to avoid the need to cast to torch.int64 at all.
      Integer throughput tends to be higher for 32-bit ints than 64-bit ints,
      not counting any possibly fewer reads we're doing due to our lower memory
      footprint.
    - V4 avoids allocating and returning a new tensor within the hash function.
      Instead, the caller will allocate two tensors; the hash function will modify
      its second argument in-place; the caller will ping-pong the two references.

Using LeetGPU's website as my benchmarking tool is hardly scientific, but, with
its leaderboard, it sure is fun. On 2025-08-23, these were the approximate
runtimes I got on a T4:
    V1: 86.75ms
    V2: 65.45ms
    V3: 32.33ms
    V4: 32.15ms
It's surprising that V4 isn't that much better than V3, and, with that small
of a difference, it's probably up to luck. V4 should be faster in principle,
and that's good enough for me with this toy problem.
"""
import torch

def fnv1a_hash_v1(x: torch.Tensor) -> torch.Tensor:
    FNV_PRIME = 16777619
    OFFSET_BASIS = 2166136261
    x_int = x.to(torch.int64)
    hash_val = torch.full_like(x_int, OFFSET_BASIS, dtype=torch.int64)
    
    for byte_pos in range(4):
        byte = (x_int >> (byte_pos * 8)) & 0xFF
        hash_val = (hash_val ^ byte) * FNV_PRIME
        hash_val = hash_val & 0xFFFFFFFF
        
    return hash_val.to(torch.int32)


def solve_v1(input: torch.Tensor, output: torch.Tensor, N: int, R: int):
    output.copy_(input)
    for _ in range(R):
        output.copy_(fnv1a_hash_v1(output))
    return


def fnv1a_hash_v2(x: torch.Tensor) -> torch.Tensor:
    """
    Now, we expect `x` to already be of type torch.int64.
    So, we can skip casting `x` every time the function is invoked.
    """
    FNV_PRIME = 16777619
    OFFSET_BASIS = 2166136261
    hash_val = torch.full_like(x, OFFSET_BASIS, dtype=torch.int64)
    
    for byte_pos in range(4):
        byte = (x >> (byte_pos * 8)) & 0xFF
        hash_val = (hash_val ^ byte) * FNV_PRIME
        hash_val = hash_val & 0xFFFFFFFF
        
    return hash_val.to(torch.int32)


def solve_v2(input: torch.Tensor, output: torch.Tensor, N: int, R: int):
    """
    Now, we allocate a tensor of type torch.int64 at the beginning, so that
    we can skip the type cast within our for-loop.
    """
    tmp = input.to(torch.int64)
    for _ in range(R):
        tmp = fnv1a_hash_v2(tmp)
    output.copy_(tmp)
    return


def fnv1a_hash_v3(x: torch.Tensor) -> torch.Tensor:
    """
    Now, we remove the need to cast to torch.int64 at all.
    With the original OFFSET_BASIS of 2166136261, we'd run into overflow
    issues since that number's larger than the max signed 32-bit int.
    Making use of two's complement, we can just use
        2166136261 % 2**32 = -2128831035
    instead. Given that the old hash function just masks off 32 bits anyway,
    we don't have to worry about wrap-around, as that's what we want.
    """
    FNV_PRIME = 16777619
    OFFSET_BASIS = -2128831035
    hash_val = torch.full_like(x, OFFSET_BASIS, dtype=torch.int32)
    
    for byte_pos in range(4):
        byte = (x >> (byte_pos * 8)) & 0xFF
        hash_val = (hash_val ^ byte) * FNV_PRIME
        
    return hash_val


def solve_v3(input: torch.Tensor, output: torch.Tensor, N: int, R: int):
    """
    Note that we use the `copy=True` kwarg, because `input` may (will) be of
    type `torch.int32`, in which case modifying `tmp` would actually modify
    `input` as well.

    Ah, the joy of Python's implicit handling of references and values.
    """
    tmp = input.to(torch.int32, copy=True)
    for _ in range(R):
        tmp = fnv1a_hash_v3(tmp)
    output.copy_(tmp)
    return


def fnv1a_hash_v4(src: torch.Tensor, dst: torch.Tensor) -> torch.Tensor:
    """
    This time, we won't bother allocating a and returning a new tensor.
    Instead, we'll modify `dst` in-place and let the caller handle allocations.
    """
    FNV_PRIME = 16777619
    OFFSET_BASIS = -2128831035  # 2166136261 % 2**32
    dst.fill_(OFFSET_BASIS)
    
    for byte_pos in range(4):
        byte = (src >> (byte_pos * 8)) & 0xFF
        dst.bitwise_xor_(byte)
        dst.mul_(FNV_PRIME)


def solve_v4(input: torch.Tensor, output: torch.Tensor, N: int, R: int):
    """
    Rather than allocating a tensor with every hash function invocation,
    we'll allocate two tensors in the beginning and then ping-pong them
    with our new hash function that modifies the second argument in-place.
    """
    res = input.to(torch.int32, copy=True)
    tmp = input.empty_like(res, dtype=torch.int32)
    for _ in range(R):
        fnv1a_hash_v4(res, tmp)
        res, tmp = tmp, res
    output.copy_(res)
    return