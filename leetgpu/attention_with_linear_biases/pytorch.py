import torch

# Q, K, V, output are tensors on the GPU
def solve(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor, output: torch.Tensor,
          M: int, N: int, d: int, alpha: float):
    Q_vw = Q.view(M, d)
    K_vw = K.view(N, d)
    V_vw = V.view(N, d)
    # (M, N) = (M, 1) - (1, N)
    delta = torch.arange(M, device=Q.device)[:, None] - torch.arange(N, device=Q.device)[None, :]

    output.copy_(
        torch.nn.functional.softmax(
            (Q_vw @ K_vw.T) / (d ** 0.5) + alpha * delta,
            dim=1
        )
        @ V_vw
    )
