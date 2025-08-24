import torch

# logits, true_labels, loss are tensors on the GPU
def solve(logits: torch.Tensor, true_labels: torch.Tensor, loss: torch.Tensor, N: int, C: int):
    """
    The dtype of `logits` is torch.float32. The dtype of `true_labels` is
    torch.int32.
    If you don't cast `true_labels` to `torch.int64`, you'll encounter an error:

        NotImplementedError: "nll_loss_forward_reduce_cuda_kernel_2d_index" not
        implemented for 'Int'

    because the underlying CUDA NLLLoss kernel expects an int64/long data type.
    """
    loss.copy_(torch.nn.functional.cross_entropy(logits, true_labels.to(torch.int64)))