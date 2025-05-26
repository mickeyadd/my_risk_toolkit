import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score

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


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix

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