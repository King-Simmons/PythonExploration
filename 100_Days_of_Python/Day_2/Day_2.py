def calculate_tip_amount(total, tip_amount):
    tip_percentage = tip_amount / 100 + 1
    tip_amount = total * tip_percentage
    return tip_amount

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_per_person = bill / people
payment = round(calculate_tip_amount(bill_per_person, tip), 2)
print(f"Each person should pay: ${payment}")
