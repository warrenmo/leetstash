import torch

# input, output are tensors on the GPU
def solve(input: torch.Tensor, output: torch.Tensor, N: int, k: int):
    output.copy_(torch.topk(input, k)[0])