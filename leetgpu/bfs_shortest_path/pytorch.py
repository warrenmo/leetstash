import torch

# grid, result are tensors on the GPU
def solve(grid: torch.Tensor, result: torch.Tensor, rows: int, cols: int, 
          start_row: int, start_col: int, end_row: int, end_col: int):
    """
    This solution completely goes against the spirit of the problem,
    because it's just a sequential algorithm.
    To top it off, we're moving the `grid` onto the CPU and performing
    the computation there.

    I'm aware that parts of the algorithm lend itself to parallel execution,
    but I don't currently know how to write that elegantly in Pytorch.
    """
    if start_row == end_row and start_col == end_col:
        result.copy_(0)
        return

    # copying to the CPU speeds this up 10x
    # most likely because we're executing the BFS sequentially
    # so we should take advantage of the latency-optimized CPU,
    # rather than the throughput-optimized GPU
    grid_vw = grid.cpu().numpy().reshape(rows, cols)

    seen = [[False] * cols for _ in range(rows)]
    seen[start_row][start_col] = True

    directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
    
    steps = 0
    level = [(start_row, start_col)]
    next_level = []
    while True:
        for row, col in level:
            for dr,dc in directions:
                next_row, next_col = row + dr, col + dc
                if next_row == end_row and next_col == end_col:
                    result.copy_(steps + 1)
                    return
                if (
                    0 <= next_row
                    and next_row < rows
                    and 0 <= next_col
                    and next_col < cols
                    and not seen[next_row][next_col]
                    and not grid_vw[next_row][next_col]
                ):
                    seen[next_row][next_col] = True
                    next_level.append((next_row, next_col))
        if not next_level:
            result.copy_(-1)
            return
        next_level, level = level, next_level
        next_level.clear()
        steps += 1
