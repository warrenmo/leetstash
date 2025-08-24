import torch

# data is a tensor on the GPU
def solve(data: torch.Tensor, N: int):
    """
    torch.sort() returns a tuple of two elements:
        (sorted tensor, indices of the elements in the original tensor)
    So for this problem, we only want the first element of the tuple.
    """
    data.copy_(torch.sort(data)[0])