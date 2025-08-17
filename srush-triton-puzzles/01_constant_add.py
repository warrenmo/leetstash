import torch
import triton
from torch import Tensor
import triton.language as tl
import jaxtyping
from jaxtyping import Float32, Int3


def add_spec(x: Float32[Tensor, "32"]) -> Float32[Tensor, "32"]:
    "This is the spec that you should implement. Uses typing to define sizes."
    return x + 10.


@triton.jit
def add_kernel(x_ptr, z_ptr, N0, B0: tl.constexpr):
    row_range = tl.arange(0, B0)
    x = tl.load(x_ptr + row_range)
    tl.store(z_ptr + row_range, x + 10
