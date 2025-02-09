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


def vector_transformation():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    plt.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

    # Define the matrix and vectors
    A = np.array([[3, 0], [0, 1]])
    v = np.array([[1], [2]])
    Av = A @ v  # Transformed vector

    # Convert to 1D arrays for plotting
    v = v.flatten()
    Av = Av.flatten()

    # Set up the plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    # Plot the original and transformed vectors
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label=r'$\mathbf{x}$')
    ax.quiver(0, 0, Av[0], Av[1], angles='xy', scale_units='xy', scale=1, color='red', label=r'$\mathbf{v}$')

    # Display the transformation equation


    tex = (r"$\quad A \mathbf{x} = \mathbf{v}  \\ \\"
        r"\begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}"
        r"\begin{bmatrix} 1 \\ 2 \end{bmatrix} = "
        r"\begin{bmatrix} 3 \\ 2 \end{bmatrix}$")
    ax.text(0.81, 0.8, tex, transform=ax.transAxes, fontsize=10,
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    # Set limits and labels
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 2.5)
    ax.set_xticks(np.arange(-0.5, 5, 1))
    ax.set_yticks(np.arange(-0.5, 3, 1))
    ax.grid(True, linestyle='--', linewidth=0.5)

    # Add legend
    ax.legend()
    plt.title(r"Matrix Transformation of a Vector $A \mathbf{x} = \mathbf{v}$")
    plt.show()


def vector_transformations():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    # Define matrix A
    A = np.array([[1, 2], [2, 4]])

    # Define x vectors
    x_1 = np.array([[2], [1]])  
    x_2 = np.array([[1], [2]]) 

    # Transform vectors
    Ax_1 = A @ x_1 
    Ax_2 = A @ x_2

    # Determine upper limits dynamically
    x_max = max(abs(Ax_1[0, 0]), abs(x_1[0, 0]), abs(Ax_1[0, 0])) + 1
    y_max = max(abs(Ax_1[1, 0]), abs(x_1[1, 0]), abs(Ax_1[1, 0])) + 1

    # Plot setup
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].set_xlim(0, x_max)
    axes[0].set_ylim(0, y_max)
    axes[1].set_xlim(0, 6)
    axes[1].set_ylim(0, 11)

    axes[0].axhline(0, color='black', linewidth=0.5)
    axes[0].axvline(0, color='black', linewidth=0.5)

    axes[0].grid(True, linestyle="--", linewidth=0.5, which='major')
    axes[0].grid(True, linestyle="--", linewidth=0.25, which='minor')

    axes[1].axhline(0, color='black', linewidth=0.5)
    axes[1].axvline(0, color='black', linewidth=0.5)
    axes[1].grid(True, linestyle='--', linewidth=0.5, which='major')
    axes[1].grid(True, linestyle=':', linewidth=0.25, which='minor')

    # Define major and minor tick locators
    major_locator = ticker.MultipleLocator(2)  # Major ticks every 2 units
    minor_locator = ticker.MultipleLocator(1)  # Minor ticks every 0.5 units

    # Set major and minor ticks for the first plot
    axes[0].xaxis.set_major_locator(major_locator)
    axes[0].xaxis.set_minor_locator(minor_locator)
    axes[0].yaxis.set_major_locator(major_locator)
    axes[0].yaxis.set_minor_locator(minor_locator)

    # Set major and minor ticks for the second plot
    axes[1].xaxis.set_major_locator(major_locator)
    axes[1].xaxis.set_minor_locator(minor_locator)
    axes[1].yaxis.set_major_locator(major_locator)
    axes[1].yaxis.set_minor_locator(minor_locator)

    # Hide minor tick labels (keep major labels)
    axes[0].tick_params(axis='both', which='minor', labelbottom=False, labelleft=False)
    axes[1].tick_params(axis='both', which='minor', labelbottom=False, labelleft=False)

    # Plot the original and transformed vectors
    axes[0].quiver(0, 0, Ax_1[0, 0], Ax_1[1, 0], color='red', angles='xy', scale_units='xy', scale=1, label='$A \mathbf{x}$')
    axes[0].quiver(0, 0, x_1[0, 0], x_1[1, 0], color='blue', angles='xy', scale_units='xy', scale=1, label='$\mathbf{x}$')
    axes[1].quiver(0, 0, Ax_2[0], Ax_2[1], angles='xy', scale_units='xy', scale=1, color='r', label='$A \mathbf{x}$')
    axes[1].quiver(0, 0, x_2[0], x_2[1], angles='xy', scale_units='xy', scale=1, color='b', label='$\mathbf{x}$')

    # Labels
    axes[0].legend(loc = "upper left")
    axes[1].legend(loc = "upper left")

    axes[0].set_title(r"Vector Transformation $\mathbf{x} = \begin{bmatrix} 2 & 1 \end{bmatrix}^\top$")
    axes[1].set_title(r"Vector Transformation $\mathbf{x} = \begin{bmatrix} 1 & 2 \end{bmatrix}^\top$")

    plt.show()
