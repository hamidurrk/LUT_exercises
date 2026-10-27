import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load digits data
digits = load_digits()

# Use digits 0 and 1 only (binary classification)
X = digits.data[(digits.target == 0) | (digits.target == 1)]
y = digits.target[(digits.target == 0) | (digits.target == 1)]
y = np.where(y == 0, -1, 1)  # convert {0, 1} → {-1, 1}

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

def plot_digits(images, labels, title, n=10):
    plt.figure(figsize=(10, 2))
    indices = np.random.choice(len(images), n, replace=False)
    for i, idx in enumerate(indices):
        plt.subplot(1, n, i + 1)
        plt.imshow(images[idx].reshape(8, 8), cmap='gray')
        plt.title(f"{'1' if labels[idx]==1 else '0'}")
        plt.axis('off')
    plt.suptitle(title)
    plt.show()

plot_digits(X_train, y_train, "Training Samples")
plot_digits(X_test, y_test, "Testing Samples")