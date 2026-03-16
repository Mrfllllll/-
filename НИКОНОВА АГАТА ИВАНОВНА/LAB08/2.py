s = input("Введите строку с датой(ами): ")

result = ""
i = 0

while i <= len(s) - 10:
    part = s[i:i+10]
    ok = True
    if not (part[0].isdigit() and part[1].isdigit()):
        ok = False
    if ok and part[2] != ".":
        ok = False
    if ok and not (part[3].isdigit() and part[4].isdigit()):
        ok = False
    if ok and part[5] != ".":
        ok = False
    if ok and not (part[6].isdigit() and part[7].isdigit() and part[8].isdigit() and part[9].isdigit()):
        ok = False

    if ok:
        result = result + "DD.MM.YYYY"
        i = i + 10
    else:
        result = result + s[i]
        i = i + 1

result = result + s[i:]

print(result)