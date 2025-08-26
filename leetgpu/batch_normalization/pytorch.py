import torch

# input, gamma, beta, output are tensors on the GPU
def solve(input: torch.Tensor, gamma: torch.Tensor, beta: torch.Tensor, 
          output: torch.Tensor, N: int, C: int, eps: float):
    input_vw = input.view(N, C)
    gamma_vw = gamma.view(1, C)
    beta_vw = beta.view(1, C)

    output.copy_(
        gamma_vw * (
            (input_vw - torch.mean(input_vw, axis=0))
            / torch.sqrt(
                torch.var(input_vw, axis=0, unbiased=False)
                + eps
            )
        )
        + beta_vw
    )