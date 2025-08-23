import torch

# input, kernel, output are tensors on the GPU
def solve(input: torch.Tensor, kernel: torch.Tensor, output: torch.Tensor,
          input_rows: int, input_cols: int, kernel_rows: int, kernel_cols: int):
    """
    Pretty much the same thing as the 1D-convolution.

    torch.nn.functional.conv2d expects 4D tensors:
      input:           (minibatch, num_in_channels, sequence_rows, sequence_cols)
      weight (kernel): (num_out_channels, num_in_channels / groups, kernel_rows, kernel_cols)
    So, we view our 1D tensors as 4D tensors for the input.
    """
    output.copy_(
        torch.nn.functional.conv2d(
            input.view(1,1,input_rows, input_cols),
            kernel.view(1,1,kernel_rows, kernel_cols)
        )
        .flatten()
    )