import torch
import triton
from torch import Tensor
import triton.language as tl
import jaxtyping
from jaxtyping import Float32, Int3


def add_vec_spec(x: Float32[Tensor, "32"], y: Float32[Tensor, "32"]) -> Float32[Tensor, "32 32"]:
    return x[None, :] + y[:, None]


@triton.jit
def add_vec_kernel(x_ptr, y_ptr, z_ptr, N0, N1, B0: tl.constexpr, B1: tl.constexpr):
    row_range = tl.arange(0, B0)[None, :]
    col_range = tl.arange(0, B1)[:, None]
    all_range = col_range * B0 + row_range

    x = tl.load(x_ptr + row_range)
    y = tl.load(y_ptr + col_range)
    tl.store(z_ptr + all_range, x + y)
    return
