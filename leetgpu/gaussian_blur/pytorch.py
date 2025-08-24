import torch

# input, kernel, output are tensors on the GPU
def solve(input: torch.Tensor, kernel: torch.Tensor, output: torch.Tensor, 
          input_rows: int, input_cols: int, kernel_rows: int, kernel_cols: int):
    """
    Nearly identical the to the regular 2D convolution, except now we pad.
    """
    output.copy_(
        torch.nn.functional.conv2d(
            input.view(1, 1, input_rows, input_cols),
            kernel.view(1, 1, kernel_rows, kernel_cols),
            padding=(kernel_rows // 2, kernel_cols // 2),
        )
        .flatten()
    )
    