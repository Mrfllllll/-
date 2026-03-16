def has_three_vowels(text):
    vowels = "аеёиоуыэюяAEЁИОУЫЭЮЯ"
    count = 0
    for ch in text:
        if ch in vowels:
            count = count + 1
            if count >= 3:
                return True
    return False


def filter_kwargs(**kwargs):
    result = {}
    for key in kwargs:
        value = kwargs[key]
        if type(value) == str:
            if has_three_vowels(value):
                result[key] = value
    return result


ans = filter_kwargs(a="привет", b="дом", c="операция", d=123, e="йцукуй")
print(ans)
