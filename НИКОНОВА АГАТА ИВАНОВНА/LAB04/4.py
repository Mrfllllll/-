nums = [10, -20, 0, 7, -4, -5, -6, 18, 3, -2, 12, 1, -19, 20, -1]
result = list(filter(lambda x: (x > -5) and (x % 2 == 0), nums))
print(result)