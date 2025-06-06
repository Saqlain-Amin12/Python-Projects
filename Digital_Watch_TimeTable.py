from datetime import datetime
import os
import time

while True:
    now = datetime.now()
    current_time = now.strftime("Time : %X")
    current_Date = now.strftime("Date : %d:%B:%Y")
    current_Day = now.strftime("Day  : %A")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(current_time)
    print(current_Date)
    print(current_Day)

    time.sleep(1)


