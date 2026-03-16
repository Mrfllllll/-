input_file = "lines.txt"
output_file = "unique.txt"

seen = set()
duplicates = []

f = open(input_file, "r", encoding="utf-8")
for line in f:
    line = line.rstrip("\n")
    if line in seen:
        duplicates.append(line)
    else:
        seen.add(line)
f.close()

f = open(input_file, "r", encoding="utf-8")
out = open(output_file, "w", encoding="utf-8")

written = set()
for line in f:
    line = line.rstrip("\n")
    if line not in written:
        out.write(line + "\n")
        written.add(line)

f.close()
out.close()
for d in duplicates:
    print(d)