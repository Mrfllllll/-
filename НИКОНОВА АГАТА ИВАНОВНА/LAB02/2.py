def analyze_text(text):
    text = text.strip()

    punctuation = ".,!?;:-()\"'"

    letters = 0
    digits = 0
    spaces = 0
    punct = 0

    for ch in text:
        if ch.isalpha():
            letters = letters + 1
        elif ch.isdigit():
            digits = digits + 1
        elif ch == " ":
            spaces = spaces + 1
        elif ch in punctuation:
            punct = punct + 1
    words_count = len(text.split())

    result = {
        "words": words_count, "letters": letters, "digits": digits, "spaces": spaces, "punctuation": punct}
    return result

s = input()
info = analyze_text(s)
print(info)