import numpy as np
import matplotlib.pyplot as plt

def sigmoid_plot():
    # Define sigmoid function
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    # Generate values for z
    z = np.linspace(-10, 10, 200)
    sigma_z = sigmoid(z)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(z, sigma_z, label=r'$\sigma(z) = \frac{1}{1+e^{-z}}$', color='red')
    plt.title('Sigmoid Function', fontsize=16)

    # Axes labels
    plt.xlabel(r'$z = x^{\top}\beta$', fontsize=14)
    plt.ylabel(r'$\sigma(z)$', fontsize=14)

    # Add horizontal line at y=0.5 for reference
    plt.axhline(0.5, color='gray', linestyle='--', linewidth=1)

    # Add vertical line at z=0 for reference
    plt.axvline(0, color='gray', linestyle='--', linewidth=1)

    # Show grid
    plt.grid(True, linestyle='--', alpha=0.6)

    # Show legend
    plt.legend(loc='upper left', fontsize=12)

    # Show plot
    plt.show()
