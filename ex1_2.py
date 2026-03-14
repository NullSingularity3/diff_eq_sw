import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def initial_condition(x: float) -> float:
    """Initial condition for the PDE."""
    return np.exp(-(x**2))


def u(x: float, t: float) -> float:
    """Solution to the PDE at position x and time t."""
    # characteristic line: x - c * t = x_0

    decay_factor = np.exp(-t)
    return decay_factor * initial_condition(x - t**2)


def animate_u_time(u: callable, x: np.ndarray, t: np.ndarray) -> None:
    """Animate the solution u(x, t) over time."""
    fig, ax = plt.subplots()
    (line,) = ax.plot(x, u(x, 0))

    def update(frame):
        line.set_ydata(u(x, frame))
        return (line,)

    ani = FuncAnimation(fig, update, frames=t, blit=True)
    plt.show()


def plot_3d(u: callable, x: np.ndarray, t: np.ndarray) -> None:
    """Plot the solution u(x, t) in 3D."""
    # TODO add characteristic lines to the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    X, T = np.meshgrid(x, t)
    Z = u(X, T)
    surf = ax.plot_surface(X, T, Z, cmap="viridis")
    plt.colorbar(surf)

    plt.xlabel("x")
    plt.ylabel("t")
    plt.title("u(x, t)")

    plt.show()


if __name__ == "__main__":
    x = np.linspace(-5, 5, 1000)
    t = np.linspace(0, 4, 1000)

    animate_u_time(u, x, t)
    plot_3d(u, x, t)
