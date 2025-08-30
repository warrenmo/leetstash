import torch

def solve(input: torch.Tensor, output: torch.Tensor, N: int, M: int, S_ROW: int, E_ROW: int, S_COL: int, E_COL: int):
    torch.sum(input[S_ROW:E_ROW+1, S_COL:E_COL+1], dim=(0, 1), out=output)