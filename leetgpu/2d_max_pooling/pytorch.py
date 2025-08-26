import torch

# input, output are tensors on the GPU
def solve(input, output, N, C, H, W, kernel_size, stride, padding):
    """
    H_out = (H - kernel_size + 2 * padding) // stride + 1
    W_out = (W - kernel_size + 2 * padding) // stride + 1
    """
    output.copy_(
        torch.nn.functional.max_pool2d(
            input.view(N, C, H, W),
            kernel_size,
            stride=stride,
            padding=padding,
        )
        .view(-1)
    )