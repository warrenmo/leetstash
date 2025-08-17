import torch
import triton
from torch import Tensor
import triton.language as tl
import jaxtyping
from jaxtyping import Float32, Int3


def sum_spec(x: Float32[Tensor, "4 200"]) -> Float32[Tensor, "4"]:
    return x.sum(1)


@triton.jit
def sum_kernel(x_ptr, z_ptr, N0, N1, T, B0: tl.constexpr, B1: tl.constexpr):
    row_pid = tl.program_id(axis=0)
    row_range = tl.arange(0, B0)[:, None] + row_pid * B0
    row_mask = row_range < N0
    acc = tl.zeros((1,B0), tl.float32)

    for col_offset in tl.static_range(0, T, B1):
        col_range = tl.arange(0, B1)[None, :] + col_offset
        range_all = row_range * T + col_range

        col_mask = col_range < T
        all_mask = row_mask & col_mask

        x = tl.load(x_ptr + range_all, all_mask)
        acc += tl.sum(x, axis=1)

    tl.store(z_ptr + row_range, acc, row_mask)

    return
