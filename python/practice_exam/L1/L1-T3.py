product = []

for i in range(1, 2+1):
    price = int(input(f"Enter the price of product {i}:\n"))
    product.append(price)

print(f"Product 1 costs {product[0]} e and product 2 costs {product[1]} e.")
print(f"The sum of the product prices is {sum(product)} euros.")
