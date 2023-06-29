# import time
# import winsound

# time_value={
#     "Hours": 3600,
#     "Minutes": 60,
#     "seconds": 1
# }
    
# def __init__(self):
#     self.total_time = 0
    
# def proces_time(self):
#     print("Insert your coding time.")
#     for t in self.time_value:
#          self.total_time += int(input(f"How many {t}? "))* self.time_value[t]
#     return self.total_time


# def count_down(self):
    
#     self.process_time()
    
#     while self.total_time:
#         hours, minutes= divmod(self.total_time, 3600)
#         mins, secs = divmod(minutes,60)
#         timer = "{:02d}: {:02d}: {:02d}".format(hours, mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         self.total_time -= 1
#     print(f'You coded for {hours} hours, {mins} minutes and {secs} seconds. Take a break')
#     winsound.Beep(1000, 2000)


# count_down()
import time
import winsound

def focus_time(user_time_seconds):
    while user_time_seconds:
        hours, remainder = divmod(user_time_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        user_time_seconds -= 1
    print(f'You coded for {hours} hours, {mins} minutes and {secs} seconds. Take a break.')
    winsound.Beep(1000, 2000)  # Beep sound (frequency, duration)

user_time_hours = float(input("Enter the time in hours: "))
user_time_minutes = float(input("Enter the time in minutes: "))

user_time_seconds = (user_time_hours * 3600) + (user_time_minutes * 60)
focus_time(user_time_seconds)
