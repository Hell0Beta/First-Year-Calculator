import time


def count_down(time_sec):

    while True:
        min, sec = divmod(time_sec, 60)
        timer = "{:d} m : {:0d}s".format(min ,sec)
        print(timer)
        time.sleep(1)
        time_sec -= 1
        if time_sec == 0:
            break

    print("TIME UP!")

timed = int(input("Enter duration:"))
count_down(timed)