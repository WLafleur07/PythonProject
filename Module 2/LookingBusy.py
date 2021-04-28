import time
import pyautogui


def make_busy():
    """Moves mouse every 10 seconds to keep apps active
    """
    print('Press CTRL-C to quit.')
    try:
        while True:
            pyautogui.moveRel(20, 0, 0.5) # moves the mous right
            pyautogui.moveRel(-20, 0, 0.5) # moves the mouse left
            time.sleep(10) # pauses the program for 10 seconds before repeating
    except KeyboardInterrupt:
        print('Process has quit...')


if __name__ == "__main__":
    make_busy()