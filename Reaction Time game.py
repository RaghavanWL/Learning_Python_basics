# Please install keyboard module to run this program. 
# Type "pip install keyboard" in command prompt to install.

import time
import keyboard
import random
g = random.randint(3,5)
print("i will say ready steady go when i say go press enter")
time.sleep(2)
print()
print()
time.sleep(1)
print("READY")
print()
print()
time.sleep(1)
print("STEADY")
print()
print()
time.sleep(g)
print("=X=X=X= GO =X=X=X=")
startingTime = time.time()
while True:
    if keyboard.is_pressed("enter"):
        endingTime = time.time()
        break
print()
print()
reactionTime = endingTime-startingTime
if reactionTime == 0.1342216968536377:
    print("IMPOSIBLE !!! YOU AND ME HAVE THE SAME REACTION TIME")
else: 
    print("Your reaction time is : ",reactionTime)
if reactionTime <= 0.1:
    print()
    print()
    print("WOW ! you have a very good reaction time")
