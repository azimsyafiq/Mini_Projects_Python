import mouse

#mouse.click("left")
#mouse.drag(0, 0, -100, -100, absolute=False, duration=0.1)
#mouse.move(-100, -200, absolute=False, duration=1)
#print(mouse.is_pressed("left"))

#listener
mouse.on_click(lambda: print("Left Button clicked"))

mouse.on_right_click(lambda: print("Right Button clicked"))

mouse.unhook_all() #remove all listeners
