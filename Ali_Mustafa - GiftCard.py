# Mustafa Ali
# Gift Card
# Block 5
# Feb 23

# This program is my own work - MA

WINNINGS = 0
TOTAL = 0


print("Welcome to the Points Redemption Portal - By Mustafa!")
while True:
    try:
        TOTAL = int(input("How many points do you have? - ")) # int makes it into an int
        break
    except ValueError: # checks for invalid input
        print("Please enter a numerical value")

#  requirment checking
if TOTAL < 2500:  # first level - NOT ELIGIBLE
    print("You are NOT eligible for a gift card, get your money up not your funny up")
elif 2500 <= TOTAL <= 7499:
    print(f"You are eligible for a 15$ gift card, BUT you need to pay 10$! :D")
    while True:
        rd = input(f"Do you wanna redeem 2500 points and pay 10$ for the 15$ gift card? (yes/no)- ")
        if rd.lower() == "yes":
            print(f"CONGRATULATIONS, you just redeemed your 15$ gift card!")
            TOTAL -= 2500
            WINNINGS += 15
            break
        elif rd.lower() == "no":
            print("Alright, Have a good day.")
            break
        else:
            print("Please enter either yes or no")
elif 7500 <= TOTAL <= 9999: # second level - 15$ possible
    print(f"You are eligible for a 15$ gift card! :D")
    while True:
        rd = input(f"Do you wanna redeem 7500 points for the 15$ gift card? (yes/no)- ")
        if rd.lower() == "yes":
            print(f"CONGRATULATIONS, you just redeemed your 15$ gift card!")
            TOTAL -= 7500
            WINNINGS += 15
            break
        elif rd.lower() == "no":
            print("Alright, Have a good day.")
            break
        else:
            print("Please enter either yes or no")
elif 10000 <= TOTAL <= 14999: # third level - 20$ possible
    print(f"You are eligible for a 20$ gift card! :D")
    while True:
        rd = input(f"Do you wanna redeem 10000 points for the 20$ gift card? (yes/no)- ")
        if rd.lower() == "yes":
            print(f"CONGRATULATIONS, you just redeemed your 20$ gift card!")
            TOTAL -= 10000
            WINNINGS += 20
            break
        elif rd.lower() == "no":
            print("Alright, Have a good day.")
            break
        else:
            print("Please enter either yes or no")
elif 15000 <= TOTAL <= 29999: # fouth level - 25$ possible
    print(f"You are eligible for a 25$ gift card! :D")
    while True:
        rd = input(f"Do you wanna redeem 15000 points for the 25$ gift card? (yes/no)- ")
        if rd.lower() == "yes":
            print(f"CONGRATULATIONS, you just redeemed your 25$ gift card!")
            TOTAL -= 15000
            WINNINGS += 25
            break
        elif rd.lower() == "no":
            print("Alright, Have a good day.")
            break
        else:
            print("Please enter either yes or no")
elif TOTAL > 30000: # fifth level - 50$ possible and offer for next purchase or food bank donation
    print(f"You are eligible for a 50$ gift card! :D")
    while True:
        rd = input(f"Do you wanna redeem 30000 points for the 50$ gift card? (yes/no)- ")
        if rd.lower() == "yes":
            print(f"CONGRATULATIONS, you just redeemed your 50$ gift card!")
            TOTAL -= 30000
            WINNINGS += 50
            break
        elif rd.lower() == "no":
            print("Alright, Have a good day.")
            break
        else:
            print("Please enter either yes or no")
    extra = input("YOU HAVE BEEN BLESSED WITH 5 DOLLARS FOR YOUR LOYALTY :D! \nWould you like to kep it for 5 dollars off on your next order or would you like to donate it to the food bank. (foodbank/keep) - ")
    if extra.lower() == "foodbank":
        print("Thank you so much for being such an upstanding citizen! we appreciate you.")
    elif extra.lower() == "keep":
        print("Revel in your greed you stingy person, you will receive $5 off on your next purchase.")

# checks if you have 0$ in winnings
if WINNINGS == 0:
    print(f"You have {TOTAL} points left and were not able to redeem a gift card D:")
else:
    print(f"You have {TOTAL} points left and you now have a {WINNINGS}$ Gift Card !!!!!!")