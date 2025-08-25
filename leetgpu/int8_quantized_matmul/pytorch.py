import torch

# A, B, C are tensors on the GPU
def solve(A: torch.Tensor, B: torch.Tensor, C: torch.Tensor, M: int, N: int,
          K: int, scale_A: float, scale_B: float, scale_C: float,
          zero_point_A: int, zero_point_B: int, zero_point_C: int):
    A_vw = A.view(M, K)
    B_vw = B.view(K, N)
    C_vw = C.view(M, N)
    tmp = torch.empty_like(C_vw, dtype = torch.float32)

    # accumulate in int32
    torch.matmul(
        (A_vw.to(torch.int32) - zero_point_A).to(torch.float32),
        (B_vw.to(torch.int32) - zero_point_B).to(torch.float32),
        out=tmp
    )

    # scale in float32
    tmp.mul_(scale_A * scale_B)
    tmp.div_(scale_C)

    # round, shift, and clamp
    tmp.round_()
    tmp.add_(zero_point_C)
    tmp.clamp_(-128, 127)

    # copy to C_vw (not C) for correct dimensions
    C_vw.copy_(tmp.to(torch.int8))
    return
