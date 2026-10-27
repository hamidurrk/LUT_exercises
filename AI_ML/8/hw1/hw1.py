import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

mtcars = pd.read_csv("./8/hw1/mtcars.csv")
X = pd.DataFrame(mtcars["wt"])
Y = pd.DataFrame(mtcars["mpg"])

model = LinearRegression()
model.fit(X, Y)
k = model.coef_[0][0]
b = model.intercept_[0]
print(f"k = {k:.4f}, b = {b:.4f}")
print(f"R^2 = {model.score(X, Y):.4f}")

plt.scatter(X, Y, label="Data")
plt.plot(X, model.predict(X), color="red", label=f"Y = {k:.3f}X + {b:.3f}")
plt.xlabel("Weight (wt)")
plt.ylabel("Gas mileage (mpg)")
plt.title("Linear regression: mpg vs. weight")
plt.legend()
plt.savefig("./8/hw1/hw1_plot.png", dpi=150)
plt.show()