"""
Exercise 2: 2D Heat Equation with FTCS Scheme.
Solves u_t = alpha * (u_xx + u_yy) on a 2D grid with Dirichlet and Neumann boundary conditions.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def initialize_grid(nx: int, ny: int, initial_temp: float = 20.0) -> np.ndarray:
    return np.full((nx, ny), initial_temp)


def apply_dirichlet_bc(
    u: np.ndarray, top_temp: float = 100.0, bottom_temp: float = 0.0
) -> np.ndarray:
    u[:, 0] = bottom_temp  # bottom
    u[:, -1] = top_temp  # top
    return u


def apply_neumann_bc(u: np.ndarray) -> np.ndarray:
    u[0, :] = u[1, :]  # left boundary
    u[-1, :] = u[-2, :]  # right boundary
    return u


def update_ftcs(u, alpha, dx, dy, dt):
    nx, ny = u.shape
    u_new = u.copy()

    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            u_new[i, j] = u[i, j] + alpha * dt * (
                (u[i + 1, j] - 2 * u[i, j] + u[i - 1, j]) / dx**2
                + (u[i, j + 1] - 2 * u[i, j] + u[i, j - 1]) / dy**2
            )

    return u_new


def run_simulation(nx=50, ny=50, nt=500, alpha=1.0):
    dx = dy = 1.0

    # Stability condition
    dt = 0.25 * min(dx**2, dy**2) / alpha

    u = initialize_grid(nx, ny)
    u = apply_dirichlet_bc(u)

    history = []

    for n in range(nt):
        u = update_ftcs(u, alpha, dx, dy, dt)

        u = apply_neumann_bc(u)
        u = apply_dirichlet_bc(u)

        if n % 10 == 0:
            history.append(u.copy())

    return history


# --------------------------------------------------
# 6. Animation
# --------------------------------------------------
def animate_solution(history):
    fig, ax = plt.subplots()
    im = ax.imshow(history[0], origin="lower", cmap="hot", vmin=0, vmax=100)

    plt.colorbar(im)

    def update(frame):
        im.set_array(history[frame])
        ax.set_title(f"Step {frame}")
        return [im]

    ani = FuncAnimation(fig, update, frames=len(history), interval=100)
    plt.show()


# --------------------------------------------------
# MAIN
# --------------------------------------------------
if __name__ == "__main__":
    history = run_simulation()
    animate_solution(history)
