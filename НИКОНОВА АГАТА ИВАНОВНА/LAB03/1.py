def longer_than_average(strings):
    if len(strings) == 0:
        return []

    total_len = 0
    for s in strings:
        total_len = total_len + len(s)

    avg = total_len/len(strings)

    result = []
    for s in strings:
        if len(s)>avg:
            result.append(s)

    return result


strings = ["кот", "дом", "флюгер", "Питер", "a"]
res = longer_than_average(strings)
print(strings, res)
