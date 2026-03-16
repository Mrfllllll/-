source_file = "source.txt"
target_file = "target.txt"

f = open(source_file, "r", encoding="utf-8")
text = f.read()
f.close()

f = open(target_file, "w", encoding="utf-8")
f.write(text)
f.close()

f = open(target_file, "r", encoding="utf-8")
text2 = f.read()
f.close()

text2 = text2.replace("cat", "dog")

f = open(target_file, "w", encoding="utf-8")
f.write(text2)
f.close()
print(text2)