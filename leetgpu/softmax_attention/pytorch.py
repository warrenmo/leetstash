import torch

# Q, K, V, output are tensors on the GPU
def solve(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor, output: torch.Tensor,
          M: int, N: int, d: int):
    scores = Q @ K.T  # (M,N)
    scores.div_(d ** 0.5)

    probs = torch.softmax(scores, dim=-1)

    out = probs @ V  # (M,d)
    output.copy_(out.reshape(-1))