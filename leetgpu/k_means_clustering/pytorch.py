"""
Thank you to user @FJN's solution for introducing me to torch.Tensor.scatter_reduce_
"""

import torch

# data_x, data_y, labels, initial_centroid_x, 
# initial_centroid_y, final_centroid_x, final_centroid_y are tensors on the GPU
def solve(data_x: torch.Tensor, 
          data_y: torch.Tensor, 
          labels: torch.Tensor, 
          initial_centroid_x: torch.Tensor, 
          initial_centroid_y: torch.Tensor, 
          final_centroid_x: torch.Tensor, 
          final_centroid_y: torch.Tensor, 
          sample_size: int, k: int, max_iterations: int):
      data = torch.stack((data_x, data_y), dim=-1)  # (sample_size, 2)
      centroids = torch.stack((initial_centroid_x, initial_centroid_y), dim=-1)  # (k, 2)

      for _ in range(max_iterations):
            dists = torch.sum(  # (sample_size, k)
                (
                    data.view(sample_size, 1, -1)  # (sample_size, 1, 2)
                    - centroids.view(1, k, -1)  # (1, k, 2)
                ).pow_(2),  # (sample_size, k, 2)
                dim=-1
            )

            labels.copy_(torch.argmin(dists, dim=1))  # (sample_size,)

            # for those like me who're unfamiliar with scatter_reduce,
            # this function:
            #   1. takes the values from `src`
            #   2. groups the values by the corresponding `index`
            #   3. reduces each group via `reduce`
            #   4. places each reduction into the input tensor at `index` (along dimension `dim`)
            # e.g.,:
            #   if dim=0, index=[[0,1],[1,0]], src=[[1, 20],[300,4_000]], reduce="sum", include_self=False
            #   then the output would be [[1,4_000],[300,20]]
            centroids.scatter_reduce_(  # (k, 2)
                dim=0,
                # (sample_size,) -> (sample_size, 1) ->(sample_size, 2)
                index=labels.view(-1, 1).broadcast_to(data.shape),
                src=data,
                reduce="mean",
                include_self=False
            )

      final_centroid_x.copy_(centroids[:, 0])
      final_centroid_y.copy_(centroids[:, 1])
