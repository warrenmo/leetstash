import torch

# input, output are tensors on the GPU
def solve(input: torch.Tensor, output: torch.Tensor, N: int, P: int):
    output_vw = output.view(N, N)
    torch.matrix_power(input.view(N, N), P, out=output_vw)