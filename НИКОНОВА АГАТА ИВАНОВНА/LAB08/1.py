s = input("Введите строку: ")
found = False

for i in range(len(s) - 13):
    part = s[i:i+14]
    ok = True

    if part[0] != "+":
        ok = False
    if ok and (not part[1].isdigit()):
        ok = False
    if ok and part[2] != "(":
        ok = False
    if ok and (not part[3].isdigit() or not part[4].isdigit() or not part[5].isdigit()):
        ok = False
    if ok and part[6] != ")":
        ok = False
    if ok and (not part[7].isdigit()):
        ok = False
    if ok and part[8] != "-":
        ok = False
    if ok and (not part[9].isdigit() or not part[10].isdigit()):
        ok = False
    if ok and part[11] != "-":
        ok = False
    if ok and (not part[12].isdigit() or not part[13].isdigit()):
        ok = False

    if ok:
        found = True
        country = part[1]
        city = part[3:6]
        abonent = part[7:]
        print("Найден номер:", part)
        print("Код страны:", country)
        print("Код города:", city)
        print("Номер абонента:", abonent)
        break

if not found:
    print("Номер не найден")