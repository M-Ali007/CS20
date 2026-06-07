# Mustafa Ali
# Mad Libs
# Block 5
# Feb 3 2026

# This program is my own work - MA

import random

print("Welcome to the Mad Libs Game!")
print("*******************************************")
name = input("Input your name - ")
place = input("Input a place - ")
pronoun = input("Input a pronoun (he / she) - ")
birth_year = int(input("Input your birth year - "))
temp = float(input("Input a Temperature(C) - "))
humidity = random.randint(20, 80)
humidity_tomorrow = humidity + random.randint(-5, 5)
object = input("Input an Object - ")
object2 = input("Input another object - ")
phrase = input("Input a suprised phrase - ")
gradYear = birth_year + 18

# Handle pronouns
if pronoun == "he":
    pronoun2 = "him"
elif pronoun == "she":
    pronoun2 = "her"

# Convert C to F
temp = float(temp * (9/5)) + 32
temp_tomorrow = temp + random.randint(-5, 5)

print("One", birth_year,"summer, I was in" ,place,"walking my pet egg", name + ". It was", temp, "degrees Fahrenheit with a humidity of", str(humidity) +"%. Suddenly, I saw a", object, "barrelling down the street! I said “", phrase + "!” as I tried to hide in the nearest", object2 + ", but could not make it in time. As the dust settled, I saw", name, "emerge from the ashes. I gazed upon", pronoun2, "agasp, feeling proud, as I know that in", str(gradYear) + ", ", pronoun, "will graduate from OSA! Once you graduate, you check the forecast and find out that tomorrow's temperature will be", str(temp_tomorrow) + "F, and that the humidity tomorrow will be", str(humidity_tomorrow) + "%")