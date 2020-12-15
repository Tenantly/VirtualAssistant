import datetime
import winsound


alarm_hour = int(input("Введите часы "))
alarm_minutes = int(input("Введите минуты "))

print(f"Установленное время сигнала: {alarm_hour}:{alarm_minutes}")

while True:

    if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:

        print("\nСигнал!")
        winsound.Beep(1000, 1000)
        break