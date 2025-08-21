import torch

# input, kernel, output are tensors on the GPU
def solve(input: torch.Tensor, kernel: torch.Tensor, output: torch.Tensor, input_size: int, kernel_size: int):
    # torch.nn.functional.conv1d expects 3D tensors:
    #   input:           (minibatch, num_in_channels, sequence_length)
    #   weight (kernel): (num_out_channels, num_in_channels / groups, kernel_length)
    # So, we view our 1D tensors as 3D tensors for the input.
    # The output will be of shape (1, 1, input_length - kernel_length + 1),
    # so we need to `squeeze`` it to shape (input_length - kernel_length + 1)
    output.copy_(torch.nn.functional.conv1d(input.view(1, 1, -1), kernel.view(1, 1, -1)).squeeze())
    return