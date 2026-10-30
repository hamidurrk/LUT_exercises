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

# ---------------------------------------------------------------
# 1. Linear regression (closed-form normal equation)
#    w = (Xb^T Xb)^+ Xb^T y, with a bias column. The pseudo-inverse is used
#    because some pixels are constant (zero after scaling), making Xb^T Xb singular.
# ---------------------------------------------------------------
def add_bias(X):
    return np.hstack([X, np.ones((X.shape[0], 1))])

def fit_linear_regression(X, y):
    Xb = add_bias(X)
    return np.linalg.pinv(Xb.T @ Xb) @ Xb.T @ y

def linreg_scores(X, w):
    return add_bias(X) @ w


# ---------------------------------------------------------------
# 2. SVM with closed-form solution (least-squares SVM, linear kernel)
#    A hard/soft-margin SVM needs a quadratic program (no closed form), so the
#    least-squares formulation is used: squared error on the margin constraints
#    y_i (w^T x_i + b) = 1 - e_i, with penalty (C/2) * sum e_i^2.
#    The KKT conditions give one linear system in (b, alpha):
#        [ 0    1^T       ] [b    ]   [0]
#        [ 1  K + I / C   ] [alpha] = [y]
#    with K = X X^T, then w = sum_i alpha_i x_i.
# ---------------------------------------------------------------
def fit_svm(X, y, C=1.0):
    n = X.shape[0]
    K = X @ X.T
    A = np.zeros((n + 1, n + 1))
    A[0, 1:] = 1
    A[1:, 0] = 1
    A[1:, 1:] = K + np.eye(n) / C
    sol = np.linalg.solve(A, np.concatenate([[0], y]))
    b, alpha = sol[0], sol[1:]
    w = X.T @ alpha
    return w, b

def svm_scores(X, w, b):
    return X @ w + b


# ---------------------------------------------------------------
# Train and evaluate
# ---------------------------------------------------------------
w_lr = fit_linear_regression(X_train, y_train)
w_svm, b_svm = fit_svm(X_train, y_train, C=1.0)

s_lr_train, s_lr_test = linreg_scores(X_train, w_lr), linreg_scores(X_test, w_lr)
s_svm_train, s_svm_test = svm_scores(X_train, w_svm, b_svm), svm_scores(X_test, w_svm, b_svm)

def accuracy(scores, y):
    return np.mean(np.where(scores >= 0, 1, -1) == y)

def confusion(scores, y):
    pred = np.where(scores >= 0, 1, -1)
    return np.array([[np.sum((y == -1) & (pred == -1)), np.sum((y == -1) & (pred == 1))],
                     [np.sum((y == 1) & (pred == -1)), np.sum((y == 1) & (pred == 1))]])

print(f"Linear regression: train acc = {accuracy(s_lr_train, y_train):.4f}, "
      f"test acc = {accuracy(s_lr_test, y_test):.4f}")
print(f"SVM (LS, C=1):     train acc = {accuracy(s_svm_train, y_train):.4f}, "
      f"test acc = {accuracy(s_svm_test, y_test):.4f}")
print("Confusion matrix, linear regression (rows: true 0/1, cols: pred 0/1):\n", confusion(s_lr_test, y_test))
print("Confusion matrix, SVM (rows: true 0/1, cols: pred 0/1):\n", confusion(s_svm_test, y_test))

# Margin of the SVM solution on the test set (distance of closest point to the hyperplane)
print(f"SVM min |w^T x + b| / ||w|| on test set: {np.min(np.abs(s_svm_test)) / np.linalg.norm(w_svm):.4f}")

# ---------------------------------------------------------------
# Visualization
# ---------------------------------------------------------------
# Test-set score distributions for both models
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)
for ax, s, name in zip(axes, [s_lr_test, s_svm_test], ["Linear regression", "SVM"]):
    ax.hist(s[y_test == -1], bins=15, alpha=0.7, label="digit 0")
    ax.hist(s[y_test == 1], bins=15, alpha=0.7, label="digit 1")
    ax.axvline(0, color="k", linestyle="--", label="decision boundary")
    ax.set_title(f"{name} (test acc {accuracy(s, y_test):.3f})")
    ax.set_xlabel("score")
axes[0].set_ylabel("count")
axes[0].legend()
plt.tight_layout()
plt.show()

# 2-D PCA projection (via SVD) of the test data with the true labels
Xc = X_train - X_train.mean(axis=0)
_, _, Vt = np.linalg.svd(Xc, full_matrices=False)
Z = (X_test - X_train.mean(axis=0)) @ Vt[:2].T
plt.figure(figsize=(5, 4))
plt.scatter(Z[y_test == -1, 0], Z[y_test == -1, 1], label="digit 0")
plt.scatter(Z[y_test == 1, 0], Z[y_test == 1, 1], label="digit 1")
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.title("Test data, PCA projection")
plt.legend()
plt.show()

# Weight vectors as 8x8 images
fig, axes = plt.subplots(1, 2, figsize=(7, 3.5))
for ax, w, name in zip(axes, [w_lr[:-1], w_svm], ["Linear regression w", "SVM w"]):
    im = ax.imshow(w.reshape(8, 8), cmap="coolwarm")
    ax.set_title(name)
    ax.axis("off")
    plt.colorbar(im, ax=ax, fraction=0.046)
plt.tight_layout()
plt.show()
