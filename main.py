# Greet user with a welcome message
print("Welcome to the Tip Calculator.\n")

# Take input from user for bill, tip, and number of people. Also; perform necessary type casting.
bill = float(input("What is the total bill amount? $"))
tip = int(input("What percent of tip would you like to give? (10, 12, 15): "))
people = int(input("How many people to split the bill? "))

# Calculate the tip amount with bill
tip_amount = tip / 100 * bill

# Calculate the total bill amount after tip
total_bill = bill + tip_amount

# Divide it by number of people
bill_per_person = total_bill / people

# Round bill_per_person so it only shows till two decimal points
bill_per_person = round(bill_per_person, 2)

# Display the output on screen
print(f"Each person should pay: ${bill_per_person}")
