import torch
import torch.nn as nn

# input, model, and output are on the GPU
def solve(input: torch.Tensor, model: nn.Module, output: torch.Tensor):
    """
    The torch.no_grad() context window ensures that no sneaky background
    computation graphs for backpropagation are built while we perform
    inference.

    Probably overkill for our purposes, but good-to-know nevertheless.
    """
    with torch.no_grad():
        output.copy_(model.forward(input))