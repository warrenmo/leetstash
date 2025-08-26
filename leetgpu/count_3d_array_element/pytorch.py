import torch

# input, output are tensors on the GPU
def solve(input: torch.Tensor, output: torch.Tensor, N: int, M: int, K: int, P: int):
    output.copy_(torch.count_nonzero(input == P))
