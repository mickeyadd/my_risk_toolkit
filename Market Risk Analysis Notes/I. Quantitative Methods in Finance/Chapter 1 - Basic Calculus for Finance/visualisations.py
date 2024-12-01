import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.integrate import quad

# Define the function to generate the 3D plot
def surface_plot():
    """ Plots a function 
    f(x, y) = x^2 * 2y - 2x - 4y
    Displays interactive surface plot
    of the graph in 3D using plotly"""

    # Define the function f(x, y) = x^2*y - 2x - 4y
    def f(x, y):
        return x**2 * y - 2*x - 4*y

    # Create a meshgrid for x and y
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # Create the 3D plot with contours and more mesh lines
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, 
                                     contours=dict(
                                         x=dict(show=True, color='black', width=1),
                                         y=dict(show=True, color='black', width=1),
                                         z=dict(show=True, color='black', width=1)
                                     ))])

    # Update layout for aesthetics
    fig.update_layout(
        template="seaborn",  
        title='Surface Plot: f(x, y) = x²y - 2x - 4y',
        scene=dict(
            xaxis_title='x',
            yaxis_title='y',
            zaxis_title="f(x, y)",
            xaxis=dict(showgrid=True, gridcolor='lightgray', nticks=10, tickvals=np.linspace(-10, 10, 5)),
            yaxis=dict(showgrid=True, gridcolor='lightgray', nticks=10, tickvals=np.linspace(-10, 10, 5)),
            zaxis=dict(showgrid=True, gridcolor='lightgray', nticks=10, tickvals=np.linspace(-1000, 1000, 5)),
            camera=dict(
                eye=dict(x=1.5, y=1.5, z = 0.5)
            ),
        ),
        autosize=False,
        width=800,
        height=800
    )
        

    # Save the plot as an HTML file
    fig.write_html("surface_plot.html")

    # Save the plot as a PNG file
    fig.write_image("surface_plot.png", width=1000, height=1000, scale=1)


    # Show the plot in the notebook
    fig.show()


# Basic function plot
def function_plot():
    def f(x):
        return 3 * x + 4
    # Quadratic Function Example
    def g(x):
        return x**2 + 8 * x - 9

    # Generate x values
    x_values = np.linspace(-10, 10, 100)
    y_f_values = f(x_values)
    y_g_values = g(x_values)

    # Plot both functions
    plt.figure(figsize=(8, 4))
    plt.plot(x_values, y_f_values, label=r"$f(x) = 3x + 4$", color="blue")
    plt.plot(x_values, y_g_values, label=r"$g(x) = x^2 + 8x - 9$", color="red")

    # Mark the roots of the function
    plt.scatter([-9, (-4/3), 1], [0, 0, 0], color=["red", "blue", "red"], marker="*", s= 10**2, zorder=5)
    # Defining x-axis values 
    plt.xticks(np.arange(-10, 11, 2))

    # Labels and grid
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot of Linear Function $f(x)$ and Quadratic Function $g(x)$")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()


def call_option_payoff():
    # Strike Price
    K = 100
    # Range of underlying prices at expiration
    S = np.linspace(50, 150, 100)

    # American call option payoff (same as European at expiration)
    payoff_call = np.maximum(S - K, 0)

    # Plot the payoff
    plt.figure(figsize=(8, 4))
    plt.plot(S, payoff_call, label='American Call Option Payoff', color='b')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
    plt.axvline(K, color='red', linestyle=':', linewidth=3, label=f'Strike Price (K={K})')  # Dotted line for strike price
    plt.xlabel('Underlying Asset Price at Expiration ($S_T$)')
    plt.ylabel('Payoff')
    plt.title('Payoff of an American Call Option at Expiration')
    plt.legend()
    plt.grid(True)
    plt.show()

# Inverse function plot
def inverse_functions():
    # Define the function and its inverse
    def f(x):
        return np.exp(x)

    def f_inverse(x):
        return np.log(x)

    # Generate x values for f(x) and a positive range for f_inverse(x) since ln(x) is only defined for x > 0
    x = np.linspace(-2, 2, 100)  # x values for f(x)
    x_inverse = np.linspace(0.1, 7, 100)  # x values for f_inverse(x), avoiding x=0 for log

    # Calculate y values for the function and its inverse
    y = f(x)
    y_inverse = f_inverse(x_inverse)

    # Plot the function, its inverse, and y = x line for symmetry
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label=r'$f(x) = e^x$', color='blue')
    plt.plot(x_inverse, y_inverse, label=r'$f^{-1}(x) = \ln(x)$', color='red')
    plt.plot(x, x, label=r'$y = x$', color='green', linestyle='--')

    # Labeling the plot
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of a Function and Its Inverse')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()



# Differentiation plot
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



# Integration Plot
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



# Random Walk plot
def random_walk():

    # Set random seed 42 (the answer to everything) for reproducibility
    np.random.seed(42)

    # Parameters
    n_steps = 1000  # Number of steps
    probability = 0.5  # Probability for each step to go up or down

    # Generate random steps: 1 (up) or -1 (down) with equal probability
    steps = np.random.choice([-1, 1], size=n_steps, p=[probability, 1 - probability])

    # Generate the positions by taking the cumulative sum of steps
    positions = np.cumsum(steps)

    # Plot the random walk
    plt.figure(figsize=(8, 4))
    plt.plot(positions, label="Random Walk")
    plt.axhline(0, color='black',linewidth=0.5)  # x-axis (starting point)
    plt.title("1,000 Step Journey of a Random Walk")
    plt.xlabel("Step")
    plt.ylabel("Position")
    plt.legend(shadow = True)
    plt.grid(True)
    plt.show()