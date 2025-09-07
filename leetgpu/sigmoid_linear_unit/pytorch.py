import torch

# input, output are tensors on the GPU
def solve(input: torch.Tensor, output: torch.Tensor, N: int):
    output.copy_(input)
    torch.nn.functional.silu(output, inplace=True)