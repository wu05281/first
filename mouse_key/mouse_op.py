#!/usr/bin/env python3
import pyautogui, time

print(pyautogui.size())
for i in range(3):
    pass
    # 将鼠标移动到指定坐标位置
    # pyautogui.moveTo(100, 100, duration=0.25)
    # pyautogui.moveTo(200, 100, duration=0.25)
    # pyautogui.moveTo(200, 200, duration=0.25)
    # pyautogui.moveTo(100, 200, duration=0.25)

    # 将鼠标移动至相对当前位置的偏移位置
    # pyautogui.moveRel(100, 0, duration=0.25)
    # pyautogui.moveRel(0, 100, duration=0.25)
    # pyautogui.moveRel(-100, 0, duration=0.25)
    # pyautogui.moveRel(0, -100, duration=0.25)

# 鼠标当前位置
print(pyautogui.position())

try:
    while True:
        time.sleep(0.5)
        print(pyautogui.position())
except KeyboardInterrupt:
    exit(0)
