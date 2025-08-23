import torch


def solve_v1(input: torch.Tensor, output: torch.Tensor, N: int):
    """
    Life is short. Use the built-ins.
    """
    output.copy_(torch.nn.functional.softmax(input))


def solve_v2(input: torch.Tensor, output: torch.Tensor, N: int):
    """
    This version's much quicker, because we write the results directly into
    `output`. In the first version, we're actually allocating a new tensor
    and then copying it into `output`.
    """
    torch.exp(input - torch.max(input), out=output)
    torch.div(output, torch.sum(output), out=output)