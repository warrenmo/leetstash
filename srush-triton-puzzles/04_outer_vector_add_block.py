import torch
import triton
from torch import Tensor
import triton.language as tl
import jaxtyping
from jaxtyping import Float32, Int3


def add_vec_block_spec(x: Float32[Tensor, "100"], y: Float32[Tensor, "90"]) -> Float32[Tensor, "90 100"]:
    return x[None, :] + y[:, None]

@triton.jit
def add_vec_block_kernel(x_ptr, y_ptr, z_ptr, N0, N1, B0: tl.constexpr, B1: tl.constexpr):
    row_pid = tl.program_id(0)
    col_pid = tl.program_id(1)

    row_range = tl.arange(0, B0)[None, :] + row_pid * B0
    col_range = tl.arange(0, B1)[:, None] + col_pid * B1
    all_range = col_range * N0 + row_range

    row_mask = row_range < N0
    col_mask = col_range < N1
    all_mask = row_mask & col_mask

    x = tl.load(x_ptr + row_range, row_mask)
    y = tl.load(y_ptr + col_range, col_mask)
    tl.store(z_ptr + all_range, x + y, all_mask)
    return
