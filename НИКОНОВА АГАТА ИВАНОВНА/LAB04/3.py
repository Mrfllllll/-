from functools import reduce
nums = list(range(1, 11))
product = reduce(lambda a, b: a * b, nums)
print(nums, product)