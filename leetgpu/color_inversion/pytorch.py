import torch

# image is a tensor on the GPU
def solve(image: torch.Tensor, width: int, height: int):
    # reshape the 1D array into a 3D array of dimensions height x width x 4
    # e.g., [0, 1, 2, 3, 4, 5, 6, 7].view(2, 1, 4) -> [[[0, 1, 2, 3]], [[0, 1, 2, 3]]]
    image = image.view(height, width, 4)
    # for the entirety of the first two dimensions
    # and up to but not including index 3 in the third dimension,
    # we'll subtract the values from 255
    image[...,:3] = 255 - image[...,:3]
    return