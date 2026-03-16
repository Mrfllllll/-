numbers = []
f = open("numbers.txt", "r", encoding="utf-8")
for line in f:
    line = line.strip()
    if line != "":
        numbers.append(float(line))
f.close()

min_num = min(numbers)
max_num = max(numbers)
avg_num = sum(numbers) / len(numbers)
print(min_num, max_num, avg_num)