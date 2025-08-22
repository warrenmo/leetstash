import torch

# input, output are tensors on the GPU
def solve(input: torch.Tensor, output: torch.Tensor, N: int):
    """
    Using pytorch's own leaky_relu will be more efficient than crafting a
    pytorch.where statement,
    provided you aren't fusing the the underlying kernels via torch.compile,
    nvFuser, Inductor, or something else.

    A pytorch.where statement is also a pretty big hammer, whereas this
    communicates intent clearly.
    """
    output.copy_(input)
    torch.nn.functional.leaky_relu(output, negative_slope=0.01, inplace=True)
    return
