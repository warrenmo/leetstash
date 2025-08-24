import torch

# A, B, C are tensors on the GPU
def solve(A: torch.Tensor, B: torch.Tensor, C: torch.Tensor, M: int, N: int, K: int, alpha: float, beta: float):
    torch.addmm(C, A, B, beta=beta, alpha=alpha, out=C)
