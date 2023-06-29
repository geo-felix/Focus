import time

def focus_time(user_time):
    while user_time:
        min, secs= divmod(user_time, 60)
        timer= '{:02d}:{:02d}'.format(min,secs)
        print(timer,end="\r")
        time.sleep(1)
        user_time -=1
    print(f"You coded for time")

user_time=int(input("Enter the time in seconds: "))

focus_time(user_time)


