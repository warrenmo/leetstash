import torch

# input is a tensor on the GPU
def solve(input: torch.Tensor, N: int):
    """
    Note that the problem specifies that we must perform the reversal in-place.
    Thus, this solution fails to meet the problem's requirements.
    I'm not currently aware of a pytorch-native method to flip the input in-place.

    This solution:
    ```
    n = input.numel()
    for left in range(n // 2):
        right = n - left - 1
        input[left], input[right] = input[right], input[left]
    ```
    fails the submission due to time-out, most likely due to the non-vectorized
    for-loop.

    Another method to reverse the vector would be to multiply the vector by
    the exchange matrix (https://en.wikipedia.org/wiki/Exchange_matrix),
    but the memtory overhead of this would negate the benefit of performing
    the reversal in-place.
    """

    input = torch.flip(input, dims=(0,))
    return

