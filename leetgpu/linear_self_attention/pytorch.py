"""
As of 2025-09-13, the function signature given in the code is incorrect:
it contains an extra, unused parameter `N: int`.

If you run the function as given, it will fail the tests.
"""
import torch

# Q, K, V, output are tensors on the GPU
def solve(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor, output: torch.Tensor,
          M: int, d: int):
    Q_phi = 1 + torch.nn.functional.elu(Q)
    K_phi = 1 + torch.nn.functional.elu(K)
    output.copy_(
        (
            Q_phi @ (K_phi.T @ V)  # (M, D) = (M, D) @ ((D, M) @ (M, D))
        ) / (
            Q_phi @ torch.sum(K_phi, dim=0, keepdim=True).T  # (M, 1) = (M, D) @ (D, 1)
        )
    )
    
