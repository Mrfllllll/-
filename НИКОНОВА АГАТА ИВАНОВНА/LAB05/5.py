from datetime import datetime
def logger(message, time_str=None):
    if time_str is None:
        time_str = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    line = "[" + time_str + "] " + message + "\n"

    f = open("log.txt", "a", encoding="utf-8")
    f.write(line)
    f.close()


msg = input()
logger(msg)

print("Сообщение записано в log.txt")