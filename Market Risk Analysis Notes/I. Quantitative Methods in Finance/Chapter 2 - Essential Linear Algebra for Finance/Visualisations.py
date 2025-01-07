import numpy as np
import matplotlib.pyplot as plt

def orthogonal_vectors():

    # Define the first vector
    vector1 = np.array([1, 5])

    # Calculate an orthogonal vector
    vector2 = np.array([-vector1[1], vector1[0]])  # Perpendicular to (1, 5)

    # Create a 2D plot
    fig, ax = plt.subplots()

    # Plot the vectors
    ax.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector (1, 5)')
    ax.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Orthogonal Vector (-5, 1)')

    # Set plot limits
    ax.set_xlim(-6, 6)
    ax.set_ylim(-4, 6)

    # Add grid, labels, and legend
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ##ax.legend()

    # Move the legend to the upper left outside the plot
    ax.legend(loc='upper left')

    # Add title
    plt.title("Orthogonal Vectors in $\mathbb{R}^2$ Space")
    plt.grid()
    plt.show()