import torch

# Q, K, V, output are tensors on the GPU
def solve(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor, output: torch.Tensor,
          N: int, d_model: int, h: int):
    partition = d_model // h

    Q_vw = Q.view(N, h, partition)
    K_vw = K.view(N, h, partition)
    V_vw = V.view(N, h, partition)

    # scores.shape == (h, N, N)
    scores = torch.matmul(
        Q_vw.transpose(0, 1),           # (h, N, partition)
        torch.permute(K_vw, (1, 2, 0))  # (h, partition, N)
    )
    scores.div_(partition ** 0.5)

    probs = torch.softmax(scores, dim=-1)

    # out.shape == (h, N, partition)
    out = torch.matmul(
        probs,                # (h, N, N)
        V_vw.transpose(0, 1)  # (h, N, partition)
    )
    output.copy_(
        out.transpose(0, 1).contiguous().view(N, d_model)
    )