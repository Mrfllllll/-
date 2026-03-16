s = input().strip()

parts = s.split(" ")

date_part = parts[0]
time_part = parts[1]

dmy = date_part.split(".")
hms = time_part.split(":")

day = dmy[0]
month = dmy[1]
year = dmy[2]

hour = hms[0]
minute = hms[1]
second = hms[2]

print("День:", day)
print("Месяц:", month)
print("Год:", year)
print("Часы:", hour)
print("Минуты:", minute)
print("Секунды:", second)