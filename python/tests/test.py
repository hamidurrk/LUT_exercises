nums = [1, 2, 3, 4, 5]
float_nums = map(float, nums)
for  num in nums:
    print(num)
print(";".join(map(str, nums)) + ";")
