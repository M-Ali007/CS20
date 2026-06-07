# Mustafa Ali
# Allowance
# Block 5
# Feb 23

# This program is my own work - MA

print("Weekly Chore Summary: ")
minutes = 0

# first questions
car = input("1. Did you clean the car? (yes or no) ").lower()  #makes input lowercase to prevent any mismatches

while car not in ["yes", "no"]:   #ensuring valid output is received
    car = input("Please enter either yes or no >:( - ")  # reprompts user

if car == "yes":  # checks yes or no
    print("75 points added, YIPPEEEEEE")
    minutes += 75
else:
    print("I'm VERY disappointed, do it next week - or else... >:(")
    print("0 points added, :(")

# second question
while(True):   # while loop to check if valid INTEGER input is recieved
    try:
        dinner = int(input("How many times did you cook dinner for the fam? Enter a Number: "))
        break
    except ValueError:
        dinner = int(input("Please input a number >:( - "))

# checks for each range of answers and gives points accordingly
if 1 <= dinner <= 2:
    print("30 points added, YIPPEEEEEE")
    minutes += 30
elif 3 <= dinner <= 4:
    print("45 points added, YIPPEEEEEE")
    minutes += 45
elif dinner >= 5:
    print("GREAT JOB!!!!! GOOD WORK :D")
    print("60 points added, YIPPEEEEEE")
    minutes += 60

# third question
multi = input("Did you mow the (a) front lawn, (b) back lawn or (c) neither - (a, b or c) ")

while multi not in ["a", "b", "c"]: # checks if input is valid
    multi = input("please input either a, b or c >:( - ") # reprompts user

if multi == 'a':
    multi2 = input("Did you remove the weeds from the front lawn? (yes/no) ").lower()

    while multi2 not in ["yes", "no"]:  # checks if input is valid
        multi2 = input("Please input either yes or no >:( - ")   # reprompts user

    if multi2 == "yes":
        print("Good Job! I'm proud of you :D")
        print("60 points added, YIPPEEEEEEEE")
        minutes += 60
    else:
        print("Well at least you did something! Great Job!")
        print("45 points added, YIPPPEEEEEEEE")
        minutes += 45

elif multi == "b":
    print("Good Job! I'm proud of you :D")
    print("90 points added, YIPPEEEEEEEE")
    minutes += 90

elif multi == "c":
    print("WHAT!!! YOU DID NO WORK??!?!?!?!")
    print("I'M VERY DISAPPOINTED IN YOU >:(")
    print("0 points added, >:(")


hourly = int(input("How much money do you make per hour? Enter a Number: "))  #Extension
moneyMade = (minutes // 60) * hourly  #calculates money made by dividing minutes to an hour and then multiplying by hourly rae
print(f"You've worked {minutes} minutes this week!")
print(f"You've earned {moneyMade}$ this week!")













