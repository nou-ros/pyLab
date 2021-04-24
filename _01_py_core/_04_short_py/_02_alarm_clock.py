from datetime import datetime
# to play the audio - pip3 install playsound
from playsound import playsound

alarm_time = input('Enter alarm time: HH:MM:SS\n')
alarm_hour = alarm_time[0:2]
# print(alarm_hour)
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper() # am/pm

print("Setting up alarm... ")

while True:
    now = datetime.now()
    # current hour
    curr_hour = now.strftime("%I")
    curr_min = now.strftime("%M")
    curr_secs = now.strftime("%S")
    curr_period = now.strftime("%p")

    conditions = [
        alarm_hour == curr_hour,
        alarm_min == curr_min,
        alarm_sec == curr_secs,
        alarm_period == curr_period
    ]

    if all(conditions):
        print('Wake Up!')
        playsound('alarm.mp3')
        break

#     if(alarm_period==current_period):
#         if(alarm_hour==current_hour):
#             if(alarm_minute==current_minute):
#                 if(alarm_seconds==current_seconds):
#                     
