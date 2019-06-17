import random
import time

print ("""
***********************************************
Number Prediction Game
***********************************************
""")
randomnumber    =   random.randint(1,50)
prediction      =   8
while   True:
    guess   =   int(input("Your Prediction:"))
    if(guess    <   randomnumber):
        print ("queriing information...")
        time.sleep(1)
        print("Please select a larger number!")
        prediction  -=  1
    elif(guess  >   randomnumber):
        print ("queriing information...")
        time.sleep(1)
        print ("Please select a smaller number!")
        prediction  -=  1
    else:
        print ("queriing information...")
        time.sleep(1)
        print ("Your Prediction is Correct!")
        break

    if(prediction   ==   0):
        print ("Your prediction is expired!")
        break
