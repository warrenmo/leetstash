import torch

# input, output are tensors on the GPU
def solve(input: torch.Tensor, output: torch.Tensor, N: int):
    """
    torch.clamp is the most direct and efficient solution to this problem,
    in my opinion: single-pass, zero extra allocations, and relatively
    clear intent.

    Other potential solutions:

    1. torch.maximum
    ```
    torch.maximum(input, torch.zeros_like(input), out=output)
    ```
    This solution wastefully creates another tensor of zeros and
    performs additional memory accesses of this tensor of zeros.

    2. torch.nn.functional.relu
    ```
    output.copy_(torch.nn.functional.relu(input))
    ```
    This solution creates a temporary tensor that holds the result
    of the ReLu before copying it into output.
    Thus, we perform an unnecessary allocation.

    3. torch.nn.functional.relu v2
    ```
    output.copy_(input)
    output.relu_()
    ```
    By copying the input into the output first and then performing the ReLu
    in-place, this solution avoids the extra allocation of the previous.
    The only potential knock against this solution is that it's more roundabout
    than torch.clamp.
    An argument could be made, though, that this solution better communicates
    intent.
    """
    torch.clamp_min(input, 0, out=output)
    return

