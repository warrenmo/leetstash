import torch
import triton
from torch import Tensor
import triton.language as tl
import jaxtyping
from jaxtyping import Float32, Int3


def mul_relu_block_back_spec(x: Float32[Tensor, "90 100"], y: Float32[Tensor, "90"],
                             dz: Float32[Tensor, "90 100"]) -> Float32[Tensor, "90 100"]:
    x = x.clone()
    y = y.clone()
    x = x.requires_grad_(True)
    y = y.requires_grad_(True)
    z = torch.relu(x * y[:, None])
    z.backward(dz)
    dx = x.grad
    return dx


@triton.jit
def mul_relu_block_back_kernel(x_ptr, y_ptr, dz_ptr, dx_ptr, N0, N1, B0: tl.constexpr, B1: tl.constexpr):
    row_pid = tl.program_id(0)
    col_pid = tl.program_id(1)

    row_range = tl.arange(0, B0)[None, :] + row_pid * B0
    col_range = tl.arange(0, B1)[:, None] + col_pid * B1
    all_range = col_range * N0 + row_range

    row_mask = row_range < N0
    col_mask = col_range < N1
    all_mask = row_mask & col_mask

    x = tl.load(x_ptr + all_range, all_mask)
    y = tl.load(y_ptr + col_range, col_mask)
    dz = tl.load(dz_ptr + all_range, all_mask)

    product = x * y
    relu_backwards = tl.where(product > 0., 1., 0.)

    tl.store(dx_ptr + all_range, relu_backwards * dz * y, all_mask)
    return
