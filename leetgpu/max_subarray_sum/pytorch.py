import torch

# input, output are tensors on the GPU
def solve(input: torch.Tensor, output: torch.Tensor, N: int, window_size: int):
    """
    We can recreate the typical two-pointers approach by instead calculating
    the entire scan / prefix sum first, and then subtracting a "lagging" subset
    of the scan from the "leading" subset of the scan.

    Steps:
    """
    # 1. calculate the prefix sum of the input
    prefix_sum = torch.empty_like(input)
    prefix_sum = torch.cumsum(input, dim=0, out=prefix_sum)

    # 2. prepend a single zero to the prefix_sum
    prefix_sum = torch.cat(
        (
            torch.zeros(1, device=prefix_sum.device, dtype=prefix_sum.dtype),
            prefix_sum
        ),
        dim=0
    )

    # 3. calculate the max over
    #       prefix_sum[i] - prefix_sum[i - window_size]
    #    for i from window_size to N
    torch.max(
        prefix_sum[window_size:] - prefix_sum[:-window_size],
        out=output
    )

