import pyautogui

green = (75, 219, 106)
counter = 0
while True:
    if counter == 5:
        break
    if pyautogui.pixel(432, 348) == green:
        pyautogui.doubleClick(432, 348)
        counter += 1
    