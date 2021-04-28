import pyautogui
from pywinauto.application import Application # module used to get ahold of the desired window
import pyperclip


def click():
    try:
        pyautogui.click()
    except:
        pass


def copy_and_past():
    """It is required to have a notepad window already open.
    When passing in the file name, just pass in 'TextName' and don't pass in '- Notepad or .txt'
    """
    document_name = input("What is the name of your file?: ")
    app = Application().connect(title=f'{document_name} - Notepad', class_name="Notepad") # Connect is used to set what application is running. 
                                                                                          # Basically connecting the program to the application
    app.top_window().set_focus()
    rect = app.window(title=f'{document_name} - Notepad', found_index=0) # Get the program by named
    rect.move_window(x=0, y=0) # Moves the window to top left of screen
    pyautogui.moveTo(100, 200) # moves the mous to 100, 200
    click() # clicks the mouse on the open app
    pyautogui.hotkey('ctrl', 'a', interval=0.10) # select all
    pyautogui.hotkey('ctrl', 'c', interval=0.1) # copy all that was selected
    print(pyperclip.paste()) # print out what was copied


if __name__ == "__main__":
    copy_and_past()