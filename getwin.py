from pynput import mouse

def on_move(x, y):
##    print('Pointer moved to {0}'.format(
    pass
##        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    #get_active_window()
    if not pressed:
        # Stop listener
        return True

def on_scroll(x, y, dx, dy):
##    print('Scrolled {0} at {1}'.format(
##        'down' if dy < 0 else 'up',
##        (x, y)))
    pass

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

#non-blocking
#listener = mouse.Listener(
#    on_move=on_move,
#    on_click=on_click,
#    on_scroll=on_scroll)
#listener.start()

    

def get_target_window(wintext):
    import win32gui
    if wintext == "":
        win2find = input('enter name of window to find')
        whnd = win32gui.FindWindowEx(None, None, None, str(win2find))
    else:
        win2find = wintext
        whnd = win32gui.FindWindowEx(None, None, None, str(wintext))
    whnd = win32gui.FindWindowEx(None, None, None, win2find)
    if not (whnd == 0):
        print('FOUND!')



