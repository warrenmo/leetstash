import torch
import triton
from torch import Tensor
import triton.language as tl
import jaxtyping
from jaxtyping import Float32, Int3


def add2_spec(x: Float32[Tensor, "200"]) -> Float32[Tensor, "200"]:
    return x + 10.

@triton.jit
def add_mask2_kernel(x_ptr, z_ptr, N0, B0: tl.constexpr):
    pid = tl.program_id(axis=0)
    row_range = tl.arange(0, B0) + pid * B0
    x = tl.load(x_ptr + row_range, row_range < N0)
    tl.store(z_ptr + row_range, x + 10, row_range < N0)
    return
