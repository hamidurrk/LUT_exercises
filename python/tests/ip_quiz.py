# 2184, 782, 257
# 691, 651, 493, 365

nums = [177, 337, 354, 365, 493, 573, 651, 691]
sum = 2200

x = 0
y = 0
z = 0
def find_sum():
    while True:
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i] + nums[j] + nums[k] == sum:
                        x = nums[i]
                        y = nums[j]
                        z = nums[k]
                        print(x, y, z)
                        return x, y, z

a, b, c, d, e = 0, 0, 0, 0, 0

def find_sum2():
    while True:
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    for l in range(len(nums)):
                        for m in range(len(nums)):
                            if nums[i] + nums[j] + nums[k] + nums[l] + nums[m] == sum:
                                a = nums[i]
                                b = nums[j]
                                c = nums[k]
                                d = nums[l]
                                e = nums[m]
                                print(a, b, c, d, e)
                                print(f"{a+b+c+d+e}")
                                return a, b, c, d, e
                            
def find_sum3():
    while True:
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    for l in range(len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == sum:
                            a = nums[i]
                            b = nums[j]
                            c = nums[k]
                            d = nums[l]
                            print(a, b, c, d)
                            print(f"{a+b+c+d}")
                            return a, b, c, d
find_sum2()