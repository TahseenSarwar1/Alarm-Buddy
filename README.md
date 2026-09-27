# ⏰ Alarm Buddy

A simple **Alarm Clock and Countdown Timer** built using Python.

## Features

* ⏰ Set an alarm for a specific time
* ⏱️ Set a countdown timer
* 🔊 Plays an MP3 sound when the alarm/timer finishes
* 💻 Works with macOS, Windows, and Linux
* 🖥️ Simple command-line interface

## Project Structure

```text
alarm-buddy/
├── alarm_clock.py
└── alarm.mp3
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd alarm-buddy
```

### 2. Run the program

**macOS / Linux:**

```bash
python3 alarm_clock.py
```

**Windows:**

```bash
python alarm_clock.py
```

No external Python packages are required.

## How to Use

When you run the program, you will see:

```text
===== ALARM BUDDY =====
1. Set Alarm
2. Set Timer
3. Exit
```

### Set Alarm

Choose `1` and enter the time in **24-hour format**:

```text
Enter alarm time (HH:MM): 07:30
```

The program will wait until the specified time and then play the alarm sound.

### Set Timer

Choose `2` and enter the duration in seconds:

```text
Enter timer duration in seconds: 60
```

The timer will count down and play the alarm sound when it reaches zero.

### Exit

Choose `3` to close the program.

## Alarm Sound

Make sure your MP3 file is named:

```text
alarm.mp3
```

and is placed in the **same folder** as `alarm_clock.py`.

## Python Concepts Used

This project helps practice:

* Variables
* Functions
* `if / elif / else`
* `while` loops
* `input()`
* `int()`
* String formatting
* `datetime`
* `time.sleep()`
* `platform`
* `subprocess`
