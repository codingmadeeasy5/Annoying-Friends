import pyautogui as pg
import random
import time
time.sleep(10)
animals = ["dog", "donkey", "bear", "monkey", "bully"]
x = random.choice(animals)
for i in range(50):
    pg.write(f"You are a {x}")
    pg.press("Enter")                   
