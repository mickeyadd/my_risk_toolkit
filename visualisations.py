import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def differentiation_plot():# Define the function f(x)
    def f(x):
        return 2 * x**3

    # Function to calculate the slope of the chord (secant line) - f'(x) approximation
    def secant_slope(x, delta_x):
        return (f(x + delta_x) - f(x)) / delta_x

    # Function to calculate the slope of the tangent line (derivative)
    def tangent_slope(x):
        return 6 * x**2

    # Fixed values
    x_value = 5.50
    delta_x = 4 # Generate x values for the function plot
    x = np.linspace(-10, 10, 1000)

    # Create the plot
    plt.figure(figsize=(8, 4))
    plt.plot(x, f(x), label=r"$f(x) = 2x^{3}$", color="blue", lw=2)

    # Plot the secant line
    plt.plot([x_value, x_value + delta_x], [f(x_value), f(x_value + delta_x)], 
            label=f"Secant line (slope ≈ {round(secant_slope(x_value, delta_x), 4)})", 
            color="black", linestyle="--")

    # Mark the key points on the function
    plt.scatter([x_value, x_value + delta_x], [f(x_value), f(x_value + delta_x)], 
                color="red", zorder=5)

    # Plot the tangent line at x_value
    tangent_line_x = np.linspace(x_value - 4, x_value + 4, 500)
    tangent_line_y = f(x_value) + tangent_slope(x_value) * (tangent_line_x - x_value)
    plt.plot(tangent_line_x, tangent_line_y, label="Tangent line", color="red", linestyle="--")

    # Plot the dashed line for secant slope representation
    secant_line_x = np.linspace(x_value, x_value + delta_x, 500)
    secant_line_y = f(x_value) + secant_slope(x_value, delta_x) * (secant_line_x - x_value)
    plt.plot(secant_line_x, secant_line_y, linestyle="dotted", color="black")#, 
    #         label=r"Secant slope: $\dfrac{f(x+\Delta x) - f(x)}{\Delta x}$")

    # Plot the horizontal line representing delta_x with bidirectional arrows
    plt.annotate(
        "", 
        xy=(x_value + delta_x, f(x_value)), 
        xytext=(x_value, f(x_value)), 
        arrowprops=dict(arrowstyle="<->", color="black", lw=1)
    )
    plt.text(x_value + delta_x / 2, f(x_value) - 150, r"$\Delta x$", ha="center", fontsize=10, color="black")

    # Plot the vertical line representing delta_y with bidirectional arrows
    plt.annotate(
        "", 
        xy=(x_value + delta_x, f(x_value + delta_x)), 
        xytext=(x_value + delta_x, f(x_value)), 
        arrowprops=dict(arrowstyle="<->", color="black", lw=1)
    )
    plt.text(x_value + delta_x + 0.2, (f(x_value) + f(x_value + delta_x)) / 2, 
            r"$f(x + \Delta x) - f(x)$", ha="left", fontsize=10, color="black")

    # Annotate the secant slope formula
    plt.text(x_value + delta_x / 2, f(x_value + delta_x) + 10, 
            r"$\dfrac{f(x + \Delta x) - f(x)}{\Delta x}$", ha="center", fontsize=10, color="black")

    # Labeling the axes and title
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Derivative Demonstration: Secant and Tangent Lines with $\Delta x$ and $\Delta f(x)$")

    # Show grid, axes, and legend
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.legend(shadow=True)

    # Show the plot
    plt.show()




def integration_plot():# Define the function f(x)
    # Define the function f(x)
    def f(x):
        return x**2 + 2 * x

    # Integration limits
    a, b = 2, 4

    # Compute the definite integral using numerical integration
    integral_value, _ = quad(f, a, b)

    # Generate x values for plotting
    x = np.linspace(-1, 5, 1000)

    # Create the plot
    plt.figure(figsize=(8, 4))
    plt.plot(x, f(x), label=r"$f(x) = x^2 + 2x$", color="blue", lw=2)

    # Highlight the area under the curve between a and b
    x_fill = np.linspace(a, b, 500)
    plt.fill_between(x_fill, f(x_fill), color='grey', alpha=0.5, 
                    label=fr"$\int_{{{a}}}^{{{b}}} f(x)dx = {integral_value:.2f}$")

    # Mark the key points on the function
    plt.scatter([a, b], [f(a), f(b)], color="black", zorder=5, s=30)

    # Labeling the axes and title
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Definite Integrals \nArea under the curve between $a$ and $b$")

    # Show grid, axes, and legend
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.legend(loc='upper left', facecolor='white', framealpha=1, shadow=True)
    plt.xticks(np.arange(0, 5.5, 0.5))
    # Show the plot
    plt.show()