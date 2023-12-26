from ahk import AHK
ahk = AHK()
ahk.mouse_move(x=100, y=100, blocking=True)
ahk.mouse_move(x=300, y=300, speed=10, blocking=True)
print(ahk.mouse_position)