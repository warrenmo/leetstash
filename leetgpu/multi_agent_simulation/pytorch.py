import torch

# agents, agents_next are tensors on the GPU
def solve(agents: torch.Tensor, agents_next: torch.Tensor, N: int):
    BLOCK_SIZE = 10_000

    agents_vw = agents.view(N, 4)
    agents_next_vw = agents_next.view(N, 4)

    curr_pos = agents_vw[:, :2]
    curr_vel = agents_vw[:, 2:]
    next_pos = agents_next_vw[:, :2]
    next_vel = agents_next_vw[:, 2:]

    for i in range(0, N, BLOCK_SIZE):
        B = min(BLOCK_SIZE, N - i)
        row_range = torch.arange(B, device=agents.device)

        # (B, N, 2) = (B, 1, 2) - (1, N, 2)
        dists = torch.norm(curr_pos[i : i + B, None] - curr_pos[None, :], dim=-1)
        dists[row_range, row_range + i] = float('inf')
        mask = dists < 5.0  # (B, N)

        num_neighbors = torch.sum(mask, dim=1)  # (B,)
        vel_avg = (mask.float() @ curr_vel) / num_neighbors[:, None]  # (B, 2)

        noop_idxs = num_neighbors == 0
        vel_avg[noop_idxs] = curr_vel[i : i + B][noop_idxs]

        curr_vel_block = curr_vel[i : i + B]
        next_vel[i : i + B] = curr_vel_block + 0.05 * (vel_avg - curr_vel_block)  # (B, 2)
        next_pos[i : i + B] = curr_pos[i : i + B] + next_vel[i : i + B]
