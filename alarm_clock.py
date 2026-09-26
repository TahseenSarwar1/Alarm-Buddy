import time
import datetime
import platform
import subprocess
import os


def play_alarm():
    system = platform.system()

    if system == "Darwin":  # macOS
        subprocess.run(["afplay", "alarm.mp3"])

    elif system == "Windows":
        import winsound
        winsound.PlaySound("alarm.mp3", winsound.SND_FILENAME)

    elif system == "Linux":
        subprocess.run(["aplay", "alarm.mp3"])


def timer(seconds):
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        print(f"\rTime remaining: {minutes:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1

    print("\nTime's up!")
    play_alarm()


def alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")

        if current_time == alarm_time:
            print("Alarm ringing!")
            play_alarm()
            break

        time.sleep(1)


def main():
    while True:
        print("\n===== ALARM CLOCK =====")
        print("1. Set Alarm")
        print("2. Set Timer")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            alarm_time = input("Enter alarm time (HH:MM): ")
            alarm(alarm_time)

        elif choice == "2":
            seconds = int(input("Enter timer duration in seconds: "))
            timer(seconds)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


main()