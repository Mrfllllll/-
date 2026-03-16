s = input("")

vowels = "аеёиоуыэюяAEЁИОУЫЭЮЯ"

result = ""

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            result = result + ch.upper()
        else:
            result = result + ch.lower()
    else:
        result = result + ch

print(result)
