from pynput.mouse import Button, Controller
import time
time.sleep(1)
mouse = Controller()
current_mouse_position = mouse.position
print(current_mouse_position)