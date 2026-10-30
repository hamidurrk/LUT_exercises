import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

all_digits = load_digits()

all_data = all_digits.data
all_labels = all_digits.target

mask_zeros = all_labels == 0
mask_ones = all_labels == 1
combined_mask = mask_zeros | mask_ones

X = all_data[combined_mask]
y = all_labels[combined_mask]

new_y = []
for label in y:
    if label == 0:
        new_y.append(-1)
    else:
        new_y.append(1)
y = np.array(new_y)

test_size_ratio = 0.2
random_seed = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_ratio, random_state=random_seed)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_train = X_train_scaled
X_test = X_test_scaled

def plot_digits(images, labels, title, n=10):
    fig = plt.figure(figsize=(10, 2))
    num_images = len(images)
    random_indices = np.random.choice(num_images, n, replace=False)
    counter = 0
    for idx in random_indices:
        counter = counter + 1
        plt.subplot(1, n, counter)
        single_image = images[idx]
        reshaped_image = single_image.reshape(8, 8)
        plt.imshow(reshaped_image, cmap='gray')
        current_label = labels[idx]
        if current_label == 1:
            label_str = '1'
        else:
            label_str = '0'
        plt.title(label_str)
        plt.axis('off')
    plt.suptitle(title)
    plt.show()

plot_digits(X_train, y_train, "Training Samples")
plot_digits(X_test, y_test, "Testing Samples")


# linear regression
def add_bias_column(X):
    num_samples = X.shape[0]
    ones_column = np.ones((num_samples, 1))
    X_with_bias = np.hstack([X, ones_column])
    return X_with_bias

def fit_linear_regression(X, y):
    X_bias = add_bias_column(X)
    X_bias_transpose = X_bias.T
    XtX = X_bias_transpose @ X_bias
    XtX_inv = np.linalg.pinv(XtX)
    Xty = X_bias_transpose @ y
    weights = XtX_inv @ Xty
    return weights

def linreg_scores(X, w):
    X_bias = add_bias_column(X)
    scores = X_bias @ w
    return scores


# SVM closed form solution
def fit_svm(X, y, C=1.0):
    n = X.shape[0]
    K = X @ X.T

    matrix_size = n + 1
    A = np.zeros((matrix_size, matrix_size))

    # fill first row
    for j in range(1, n + 1):
        A[0][j] = 1

    # fill first col
    for i in range(1, n + 1):
        A[i][0] = 1

    # fill the rest
    identity_matrix = np.eye(n)
    penalty = 1.0 / C
    K_plus_I = K + identity_matrix * penalty
    for i in range(n):
        for j in range(n):
            A[i + 1][j + 1] = K_plus_I[i][j]

    rhs_first = np.array([0])
    rhs_rest = y
    rhs = np.concatenate([rhs_first, rhs_rest])

    solution = np.linalg.solve(A, rhs)

    b_value = solution[0]
    alpha_values = solution[1:]

    w_vector = X.T @ alpha_values

    return w_vector, b_value

def svm_scores(X, w, b):
    dot_products = X @ w
    scores = dot_products + b
    return scores


# train both models
w_lr = fit_linear_regression(X_train, y_train)
C_value = 1.0
w_svm, b_svm = fit_svm(X_train, y_train, C=C_value)

# get scores for everything
s_lr_train = linreg_scores(X_train, w_lr)
s_lr_test = linreg_scores(X_test, w_lr)
s_svm_train = svm_scores(X_train, w_svm, b_svm)
s_svm_test = svm_scores(X_test, w_svm, b_svm)


def accuracy(scores, y):
    num_correct = 0
    total = len(scores)
    for i in range(total):
        if scores[i] >= 0:
            predicted = 1
        else:
            predicted = -1
        if predicted == y[i]:
            num_correct = num_correct + 1
    result = num_correct / total
    return result

def confusion(scores, y):
    true_neg = 0
    false_pos = 0
    false_neg = 0
    true_pos = 0

    for i in range(len(scores)):
        if scores[i] >= 0:
            pred = 1
        else:
            pred = -1

        actual = y[i]

        if actual == -1 and pred == -1:
            true_neg = true_neg + 1
        elif actual == -1 and pred == 1:
            false_pos = false_pos + 1
        elif actual == 1 and pred == -1:
            false_neg = false_neg + 1
        elif actual == 1 and pred == 1:
            true_pos = true_pos + 1

    row1 = [true_neg, false_pos]
    row2 = [false_neg, true_pos]
    conf_matrix = np.array([row1, row2])
    return conf_matrix


lr_train_acc = accuracy(s_lr_train, y_train)
lr_test_acc = accuracy(s_lr_test, y_test)
svm_train_acc = accuracy(s_svm_train, y_train)
svm_test_acc = accuracy(s_svm_test, y_test)

print("Linear regression: train acc = " + str(round(lr_train_acc, 4)) + ", test acc = " + str(round(lr_test_acc, 4)))
print("SVM (LS, C=1):     train acc = " + str(round(svm_train_acc, 4)) + ", test acc = " + str(round(svm_test_acc, 4)))

conf_lr = confusion(s_lr_test, y_test)
conf_svm = confusion(s_svm_test, y_test)
print("Confusion matrix, linear regression (rows: true 0/1, cols: pred 0/1):")
print(conf_lr)
print("Confusion matrix, SVM (rows: true 0/1, cols: pred 0/1):")
print(conf_svm)

# margin calculation
abs_scores = []
for score in s_svm_test:
    abs_scores.append(abs(score))
min_abs_score = min(abs_scores)
w_norm = np.linalg.norm(w_svm)
margin = min_abs_score / w_norm
print("SVM min |w^T x + b| / ||w|| on test set: " + str(round(margin, 4)))


# plots
fig1 = plt.figure(figsize=(10, 3.5))

ax1 = fig1.add_subplot(1, 2, 1)
scores_class0_lr = []
scores_class1_lr = []
for i in range(len(s_lr_test)):
    if y_test[i] == -1:
        scores_class0_lr.append(s_lr_test[i])
    else:
        scores_class1_lr.append(s_lr_test[i])
ax1.hist(scores_class0_lr, bins=15, alpha=0.7, label="digit 0")
ax1.hist(scores_class1_lr, bins=15, alpha=0.7, label="digit 1")
ax1.axvline(0, color="k", linestyle="--", label="decision boundary")
lr_test_acc2 = accuracy(s_lr_test, y_test)
ax1.set_title("Linear regression (test acc " + str(round(lr_test_acc2, 3)) + ")")
ax1.set_xlabel("score")
ax1.set_ylabel("count")
ax1.legend()

ax2 = fig1.add_subplot(1, 2, 2)
scores_class0_svm = []
scores_class1_svm = []
for i in range(len(s_svm_test)):
    if y_test[i] == -1:
        scores_class0_svm.append(s_svm_test[i])
    else:
        scores_class1_svm.append(s_svm_test[i])
ax2.hist(scores_class0_svm, bins=15, alpha=0.7, label="digit 0")
ax2.hist(scores_class1_svm, bins=15, alpha=0.7, label="digit 1")
ax2.axvline(0, color="k", linestyle="--", label="decision boundary")
svm_test_acc2 = accuracy(s_svm_test, y_test)
ax2.set_title("SVM (test acc " + str(round(svm_test_acc2, 3)) + ")")
ax2.set_xlabel("score")

plt.tight_layout()
plt.savefig("./8/hw2/hw2_plot.png", dpi=150)
plt.show()

# PCA plot
mean_train = X_train.mean(axis=0)
X_centered = X_train - mean_train
U_matrix, S_values, Vt_matrix = np.linalg.svd(X_centered, full_matrices=False)
first_two_components = Vt_matrix[:2]
X_test_centered = X_test - mean_train
Z = X_test_centered @ first_two_components.T

Z_class0_pc1 = []
Z_class0_pc2 = []
Z_class1_pc1 = []
Z_class1_pc2 = []

for i in range(len(Z)):
    if y_test[i] == -1:
        Z_class0_pc1.append(Z[i][0])
        Z_class0_pc2.append(Z[i][1])
    else:
        Z_class1_pc1.append(Z[i][0])
        Z_class1_pc2.append(Z[i][1])

plt.figure(figsize=(5, 4))
plt.scatter(Z_class0_pc1, Z_class0_pc2, label="digit 0")
plt.scatter(Z_class1_pc1, Z_class1_pc2, label="digit 1")
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.title("Test data, PCA projection")
plt.legend()
plt.savefig("./8/hw2/hw2_pca_plot.png", dpi=150)
plt.show()

# weight images
w_lr_no_bias = w_lr[:-1]
w_lr_image = w_lr_no_bias.reshape(8, 8)
w_svm_image = w_svm.reshape(8, 8)

fig2, axes2 = plt.subplots(1, 2, figsize=(7, 3.5))
im1 = axes2[0].imshow(w_lr_image, cmap="coolwarm")
axes2[0].set_title("Linear regression w")
axes2[0].axis("off")
plt.colorbar(im1, ax=axes2[0], fraction=0.046)

im2 = axes2[1].imshow(w_svm_image, cmap="coolwarm")
axes2[1].set_title("SVM w")
axes2[1].axis("off")
plt.colorbar(im2, ax=axes2[1], fraction=0.046)

plt.tight_layout()
plt.savefig("./8/hw2/hw2_weights_plot.png", dpi=150)
plt.show()
