import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn import datasets

# Plot the original and standardised data transformation
def standardisation_plot(original_data, standardised_data):
    plt.figure(figsize=(14, 5))

    # Before Standardisation
    plt.subplot(1, 2, 1)
    sns.histplot(original_data.flatten(), bins=50, color='salmon', kde=True)
    plt.title('Before Standardisation')
    plt.xlabel('Original Feature Values')
    plt.ylabel('Frequency')
    plt.grid(True)

    # After Standardisation
    plt.subplot(1, 2, 2)
    sns.histplot(standardised_data.flatten(), bins=50, color='mediumseagreen', kde=True)
    plt.title('After Standardisation')
    plt.xlabel('Standardised Feature Values')
    plt.ylabel('Frequency')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Plot the sigmoid function
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

# Plot the model weights based on their magnitude and feature names as a bar chart
def plot_model_weights_gradient(weights, feature_names, title='Model Weights', sort_by_abs=True, palette='viridis'):
    """
    Plot model weights as a horizontal bar chart with gradient color intensity based on weight magnitude.

    Parameters:
    -----------
    weights : array-like
        Array of model weights.
    feature_names : list
        List of feature names corresponding to the weights.
    title : str
        Title of the plot.
    sort_by_abs : bool
        Whether to sort bars by absolute weight values.
    palette : str
        Seaborn continuous palette name for coloring bars by magnitude.
    """
    # Create DataFrame
    params_df = pd.DataFrame({
        'Feature': [str(f).replace('_', ' ').title() for f in feature_names],
        'Weight': weights.flatten()
    })

    # Optionally sort by absolute weight
    if sort_by_abs:
        params_df = params_df.reindex(params_df['Weight'].abs().sort_values(ascending=False).index)

    # Normalize absolute weights to [0,1] for coloring
    norm = plt.Normalize(params_df['Weight'].abs().min(), params_df['Weight'].abs().max())
    colors = sns.color_palette(palette, as_cmap=True)(norm(params_df['Weight'].abs()))

    # Plot
    sns.set_theme(style="white")
    plt.figure(figsize=(10, 8))
    bars = plt.barh(
        params_df['Feature'],
        params_df['Weight'],
        color=colors
    )

    plt.title(title, fontsize=14)
    plt.xlabel('Weight Value')
    plt.ylabel('Feature')
    plt.gca().invert_yaxis()  # Most important at top
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


# Plot the losses over training the model
def loss_plot(losses):
    plt.plot(losses)
    plt.xlabel("Epoch")
    plt.ylabel("Binary Cross-Entropy Loss")
    plt.title("Loss over Training")
    plt.show()

# Plot a confusion matrix
def plot_confusion_matrix(y_true, y_pred, class_names=None, title='Confusion Matrix', cmap='Blues', normalize=False):
    """
    Plots a confusion matrix using seaborn heatmap.

    Parameters:
    -----------
    y_true : array-like
        True class labels.
    y_pred : array-like
        Predicted class labels.
    class_names : list, optional
        Class names for axis ticks. If None, uses numeric labels.
    title : str
        Title of the plot.
    cmap : str
        Colormap for the heatmap.
    normalize : bool
        If True, displays percentages instead of counts.

    Returns:
    --------
    None
    """
    labels = np.unique(np.concatenate((y_true, y_pred)))
    cm = confusion_matrix(y_true, y_pred, labels=labels)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    # Proper-case the class names if provided
    if class_names is not None:
        class_names = [str(name).title() for name in class_names]
    else:
        class_names = labels

    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='.2f' if normalize else 'd', cmap=cmap,
                xticklabels=class_names if class_names is not None else labels,
                yticklabels=class_names if class_names is not None else labels)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(title)
    plt.tight_layout()
    plt.show()


# Plot the ROC curve and display the AUC
def plot_roc_curve(y_true, y_scores, title='ROC Curve'):
    """
    Plots ROC Curve and displays ROC AUC score.

    Parameters:
    -----------
    y_true : array-like
        True class labels.
    y_scores : array-like
        Predicted probabilities or decision scores.
    title : str
        Title of the plot.

    Returns:
    --------
    None
    """
    fpr, tpr, thresholds = roc_curve(y_true, y_scores)
    roc_auc = roc_auc_score(y_true, y_scores)

    plt.figure(figsize=(6, 5))
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    plt.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(title)
    plt.legend(loc="lower right")
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()

    print(f"ROC AUC Score: {roc_auc:.4f}")

# Plot the California housing data
def cal_housing_plot(data):
    fig = px.scatter_mapbox(
        data,
        lat="Latitude",
        lon="Longitude",
        color="MedHouseVal_Dollars",
        color_continuous_scale="Viridis",
        zoom=5,
        height=900,
        width=1500,
        mapbox_style="carto-positron",
        title="California Housing Values Heatmap",
    )

    # Customize colorbar ticks and labels
    fig.update_layout(
        coloraxis_colorbar=dict(
            title="Median House Value ($)",
            tickvals=[100000, 300000, 500000],
            ticktext=["100k", "300k", "500k"],
            ticks="outside",
            ticklen=8,
            tickfont=dict(size=12),
        )
    )
    # Export to HTML file
    #fig.write_html("california_house_values_heatmap_plotly.html")

    fig.show()

# Plot Lasso Feature Importance
def lasso_features_plot(importance_df):

    plt.figure(figsize=(10, 6))
    sns.barplot(
        y='Feature',
        x='Coefficient',
        data=importance_df,
        hue='Abs_Coefficient',        # numeric hue to get gradient colors
        palette='viridis',            # continuous colormap
        dodge=False,
        legend=False                  # hide the legend
    )

    plt.xlabel('Coefficient Value')
    plt.title('Feature Importance (Lasso Regression)')
    plt.tight_layout()
    plt.show()


def plot_optimised_betas(beta_hist, loss_hist):
    """
    Plots an interactive 3D line plot of epochs vs loss vs beta values for each beta coefficient.

    Parameters:
    -----------
    beta_hist : list or array-like
        List of arrays containing beta values at each epoch (shape: n_features x 1).
    loss_hist : list or array-like
        List of loss values for each epoch.
    epochs : list or array-like
        List of epoch numbers (same length as loss_hist and beta_hist)

    Returns:
    --------
    None (shows interactive plot)
    """

    import plotly.graph_objects as go
    import numpy as np


    epochs = np.arange(len(loss_hist))
    betas_flat = np.array([b.flatten() for b in beta_hist])

    fig = go.Figure()

    for beta_idx in range(betas_flat.shape[1]):
        beta_values = betas_flat[:, beta_idx]

        hover_template = (
            "Epoch: %{x}<br>" +
            "Loss: %{y:.4f}<br>" +
            f"Beta β{beta_idx}: " + "%{z:.4f}<extra></extra>"
        )

        fig.add_trace(go.Scatter3d(
            x=epochs,
            y=loss_hist,
            z=beta_values,
            mode='lines+markers',
            name=f'β{beta_idx}',
            line=dict(width=2),
            marker=dict(size=3),
            hovertemplate=hover_template
        ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(title='Epoch'),
            yaxis=dict(title='Loss (Log-Likelihood)'),
            zaxis=dict(title='Beta Coefficient')
        ),
        margin=dict(l=0, r=0, b=0, t=50),
        showlegend=True
    )

    fig.show()

    # Export to HTML file
    # fig.write_html("beta_optimisation_plotly.html")




def binary_boundary_plot(show=True):
    """
    Plot binary logistic regression decision boundary on the Iris dataset 
    (Setosa vs Versicolor using sepal length and sepal width).
    """
    # Load Iris data
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = iris.target

    # Keep only Setosa (0) and Versicolor (1)
    mask = (y == 0) | (y == 1)
    X_bin = X[mask]
    y_bin = y[mask]

    # Fit binary logistic regression
    model = LogisticRegression()
    model.fit(X_bin, y_bin)

    # Create grid
    xx, yy = np.meshgrid(np.linspace(X_bin[:, 0].min()-0.5, X_bin[:, 0].max()+0.5, 300),
                         np.linspace(X_bin[:, 1].min()-0.5, X_bin[:, 1].max()+0.5, 300))
    grid = np.c_[xx.ravel(), yy.ravel()]

    # Predict probabilities
    probs = model.predict_proba(grid)[:, 1].reshape(xx.shape)

    # Plot
    plt.figure(figsize=(8,6))
    plt.contourf(xx, yy, probs, cmap='coolwarm', alpha=0.3, levels=20)
    plt.contour(xx, yy, probs, levels=[0.5], colors='black', linewidths=2)
    plt.scatter(X_bin[:, 0], X_bin[:, 1], c=y_bin, cmap='bwr', edgecolor='k')
    plt.title("Binary Logistic Regression (Setosa vs Versicolor)")
    plt.xlabel("Sepal length (cm)")
    plt.ylabel("Sepal width (cm)")
    plt.colorbar(label="P(Class Versicolor)")
    if show:
        plt.show()
