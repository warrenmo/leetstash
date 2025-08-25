import torch

# X, y, beta are tensors on the GPU
def solve_v1(X: torch.Tensor, y: torch.Tensor, beta: torch.Tensor, n_samples: int, n_features: int):
    """
    Slightly slower, perhaps due to all the extra return values (that we don't need)
    of torch.linalg.lstsq.
    """
    beta.copy_(
        torch.linalg.lstsq(
            X.view(n_samples, n_features),
            y
        )
        [0]  # return type is tuple: (solution, residuals, rank, singular values)
    )

# X, y, beta are tensors on the GPU
def solve_v2(X: torch.Tensor, y: torch.Tensor, beta: torch.Tensor, n_samples: int, n_features: int):
    X_vw = X.view(n_samples, n_features)
    beta.copy_(torch.linalg.solve(X_vw.T @ X_vw, X_vw.T @ y))
