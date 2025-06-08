import numpy as np
import pandas as pd

class Logistic_Regression_Scratch:


    @staticmethod
    def check_class_balance(y):
        """
        Print class counts with labels Malignant (1) and Benign (0),
        and the minority-to-majority imbalance ratio.

        Parameters:
        y (pandas Series or numpy array): Target labels.

        Returns:
        float: Minority-to-majority class ratio.
        """
        from collections import Counter

        counts = Counter(y)
        categories = list(counts.values())
        imbalance_ratio = min(categories) / max(categories)

        print("Class counts:")
        print(f"Malignant (1): {counts.get(1, 0)}")
        print(f"Benign    (0): {counts.get(0, 0)}")
        print(f"\nMinority-to-majority class ratio: {imbalance_ratio:.2f}")

        return imbalance_ratio
    
    @staticmethod
    def train_test_split(X, y, test_size=0.2, random_state=None):
        """
        Splits feature and target arrays into training and testing sets.

        Parameters:
        -----------
        X : np.ndarray
            Feature array.
        y : np.ndarray
            Target array.
        test_size : float, optional (default=0.2)
            Proportion of the dataset to include in the test split.
        random_state : int, optional
            Random seed for reproducibility.

        Returns:
        --------
        X_train, X_test, y_train, y_test : tuple
            The split feature and target arrays for training and testing.
        """
        if random_state is not None:
            np.random.seed(random_state)

        n_samples = X.shape[0]
        indices = np.arange(n_samples)
        np.random.shuffle(indices)

        test_count = int(n_samples * test_size)
        test_indices = indices[:test_count]
        train_indices = indices[test_count:]

        X_train = X[train_indices]
        X_test  = X[test_indices]
        y_train = y[train_indices]
        y_test  = y[test_indices]

        return X_train, X_test, y_train, y_test
    
    @staticmethod
    def standardize_train_test(X_train, X_test):
        """
        Standardises the training and testing sets by subtracting the 
        mean of the training data and dividing the result by the 
        standard deviation of the training data for each observation
        in the training and test sets.

        Parameters:
        -----------
        X_train : np.ndarray
            Training array.
        X_test : np.ndarray
            Test array.

        Returns:
        --------
        Standardised training and test data using the mean and standard deviation
        of the training set.
        """
        mean = np.mean(X_train, axis=0)
        std = np.std(X_train, axis=0)

        X_train_st = (X_train - mean) / std
        X_test_st = (X_test - mean) / std  # use training mean and std

        return X_train_st, X_test_st
    
    def sigmoid(z):
        """
        Compute the sigmoid (logistic) function for the input array z.

        The sigmoid function maps any real-valued number into the range (0, 1),
        often used to model probabilities in logistic regression.

        Parameters:
        -----------
        z : float or np.ndarray
            Input value or array of values.

        Returns:
        --------
        np.ndarray or float
            The sigmoid of the input, with values clipped to avoid numerical overflow.

        Notes:
        ------
        Input z is clipped between -500 and 500 to prevent overflow errors in the 
        exponential function.

        The small epsilon (1e-15) can be used later to avoid issues when
        applying log on predicted probabilities close to 0 or 1.
        """
        # Clip z to prevent overflow in exp
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    epsilon = 1e-15

    def compute_intercept_only(self, y):
        """
        Calculate and print the intercept-only log-odds for the positive class.

        Parameters:
        -----------
        y : np.ndarray or pd.Series
            Binary target array with values 0 and 1.

        Returns:
        --------
        float
            The intercept-only log-odds value.
        """
        positive_rate = np.mean(y == 1)
        epsilon = 1e-15
        positive_rate = np.clip(positive_rate, epsilon, 1 - epsilon)
        intercept_only = np.log(positive_rate / (1 - positive_rate))
        print(f"Intercept-only log-odds (bias initialization): {intercept_only:.4f}")
        return intercept_only