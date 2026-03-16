file_name = "text.txt"
new_line = input()

f = open(file_name, "a", encoding="utf-8")
f.write(new_line + "\n")
f.close()

print("\nСодержимое файла после добавления:")
f = open(file_name, "r", encoding="utf-8")
for line in f:
    print(line.rstrip())
f.close()