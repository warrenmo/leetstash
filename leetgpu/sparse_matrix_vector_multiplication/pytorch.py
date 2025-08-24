import torch

# A, x, y are tensors on the GPU
def solve(A: torch.Tensor, x: torch.Tensor, y: torch.Tensor, M: int, N: int, nnz: int):
    """
    It makes more mathematical sense (to me) that we'd need to write `x1 as
    `x.view(N, 1)` for "proper" matrix multiplication. But if you do, then
    you'll have to call `y.squeeze_()`, because `y` will be of shape (N,1)
    rather than (1,N), which is what we want.

    If you leave `x` as-is, then pytorch will understand your intention and `y`
    will be of shape (1,N).
    """
    torch.matmul(A.view(M, N), x, out=y)