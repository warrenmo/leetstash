import torch

# input, output are tensors on the GPU
def solve(input: torch.Tensor, gamma: torch.Tensor, beta: torch.Tensor, 
          output: torch.Tensor, N: int, eps: float):
    output.copy_(
        torch.nn.functional.rms_norm(
            input,
            input.shape,
            weight=gamma * torch.ones_like(input),
            eps=eps
        )
        + beta
    )
