import torch

# input, output are tensors on the GPU
def solve(input: torch.Tensor, output: torch.Tensor, N: int):
    output.copy_(input[:N // 2])
    torch.nn.functional.silu(output, inplace=True)
    output.mul_(input[N // 2:])