#-------------------------------------
#  Name:     Mustafa
#  Program:  Ali_Mustafa - Weather Predictor.py
# ------------------------------------
# This program converts F to C and predicts tomorrow's temperature.
# Test on:   68 -> 20	50 -> 10	 41 -> 5	 32 -> 0

# Obtain the temperature for today in Fahrenheit
today = input("What is today's date? ")
fahrenheit = input(today + ": Enter the temperature in fahrenheit: ")

# Convert the temperature from Fahrenheit to Celsius
celsius = (int(fahrenheit) - 32) * 5.0 / 9.0

# Generate a random number between -5 and +5
import random
change = random.randint(-5, 5)

# Calculate the weather tomorrow using the predicted change
tomorrow = celsius + change

# Calculate Humidity
humidity = random.randint(10, 80)

# Calculate tomorrow's Humidity
humidity_tomorrow = humidity + random.randint(-5, 5)

# Display the results
print()   # Print a blank line
print(fahrenheit, "degrees F equals", celsius, "degrees C.")
print("Today's Humidity is", str(humidity) + "%")
print("Tomorrow the temperature will change by", change, "degrees to become", tomorrow, "degrees C and tomorrow's humidity will be", str(humidity_tomorrow) + "%")
