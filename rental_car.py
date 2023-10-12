import sys

# Collect input from customer - Rental type
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n") # Assigning a string value to a variable

# Decode input and direct to correct function
if rentalCode == "W":
  rentalPeriod = int(input("Number of Weeks Rented:\n")) # Assigning a numerical value to a variable
  
elif rentalCode == "D":
  rentalPeriod = int(input("Number of Days Rented:\n")) # Modifying variables with data-type-appropriate operators

else:
  rentalPeriod = int(input("Number of Days Rented:\n"))

# Variables to calculate charges
budgetCharge = 60
baseCharge = rentalPeriod * budgetCharge

# Collect input from customer - Odometer
odoStart = int(input("Starting Odometer Reading:\n"))
odoEnd = int(input("Ending Odometer Reading:\n"))
totalMiles = odoEnd - odoStart

# Calculate charges
if rentalCode == "B": # If statement
  mileCharge = totalMiles * 0.25

elif rentalCode == "D": # Elif statement
  averageDayMiles = totalMiles / rentalPeriod
  if averageDayMiles <= 100:
    mileCharge = 0
  else: 
    extraMiles = averageDayMiles - 100
    mileCharge = extraMiles * 0.25

else: # Else statement
  averageDayMiles = totalMiles / rentalPeriod
  if averageDayMiles <= 900:
    mileCharge = 0
  else:
    mileCharge = 100 * rentalPeriod

# Print Summary
print("Rental Summary")
print("Rental Code: " + rentalCode)
print("Rental Period: " + str(rentalPeriod))
print("Starting Odometer: " + str(odoStart))
print("Ending Odometer: " + str(odoEnd))
print("Miles Driven: " + str(totalMiles))
print("Amount Due: $" + "{:.2f}".format(baseCharge + mileCharge))