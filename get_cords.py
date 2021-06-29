import win32api, win32con

x_pad = 390
y_pad = 197


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)


get_cords()
