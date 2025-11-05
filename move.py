import pyautogui
import time
import threading
import keyboard

running = True

def move_mouse():
    global running
    print("Automation started. Press 'p' to pause/resume, 'q' to quit.")
    paused = False
    while running:
        if keyboard.is_pressed('q'):
            print("Quitting...")
            running = False
            break
        if keyboard.is_pressed('p'):
            paused = not paused
            print("Paused" if paused else "Resumed")
            time.sleep(1)  # prevent rapid toggling
        if not paused:
            pyautogui.move(25, 0)   # move right
            pyautogui.move(-25, 0)  # move left
        time.sleep(300)  # 5 minutes (300 seconds)

thread = threading.Thread(target=move_mouse)
thread.start()
