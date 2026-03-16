numbers = [1, 2, 2, 3, 3, 3, 5, 5, 10]

counts = {}

for x in numbers:
    if x in counts:
        counts[x] = counts[x] + 1
    else:
        counts[x] = 1

for x in counts:
    print(x, counts[x])
