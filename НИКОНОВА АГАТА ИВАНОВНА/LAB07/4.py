import sys

input_file = sys.argv[sys.argv.index("--input") + 1]
output_file = sys.argv[sys.argv.index("--output") + 1]

f = open(input_file, "r", encoding="utf-8")
data = f.read()
f.close()

f = open(output_file, "w", encoding="utf-8")
f.write(data)
f.close()
