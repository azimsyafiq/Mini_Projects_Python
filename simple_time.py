import datetime

alarmHour = int(input("What hour do you want to wake up? "))
alarmMinute = int(input("What minute do you want to wake up? "))
amPm = str(input("Am or Pm? ").lower())

if amPm == 'pm':
    alarmHour += 12

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute:
        print('WAKE UP!')
        break

print('Alarm dismissed.')