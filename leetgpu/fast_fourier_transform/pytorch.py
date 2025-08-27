import torch

# signal and spectrum are device pointers
def solve(signal: torch.Tensor, spectrum: torch.Tensor, N: int):
    spectrum_complex = torch.fft.fft(
        torch.view_as_complex(signal.view(N, 2))
    )
    spectrum.copy_(torch.view_as_real(spectrum_complex).flatten())