# Simple Coffee Shop Program

print("========== Welcome! ==========")

# Ask for user's information
first_name= input("Enter your name here -->: ")
last_name = input("Enter your surname here -->: ")

print("\n======= Coffee List =======")
print("Lipton")
print("Coffee")
print("Milk")
print("Chocolate Coffee\n")

# Ask for the desired drink
drink_mark = input("Enter the name of the drink you want -->: ")

unit_price = 200
print(f"\nThank you! One unit of {drink_mark} costs {unit_price} FCFA.")

# Ask for the quantity
number_of_unit = int(input("\nHow many do you want? -->: "))
total = unit_price * number_of_unit
print(f"\nOk, that will cost you {total} FCFA.")

# Ask for payment
client_money = float(input("Please give me the money -->: "))
change = client_money - total

# Print receipt
print(f"\nYou took {number_of_unit} unit(s) of {drink_mark}.")
print(f"Your total expenses are {total} FCFA.")
print(f"You gave {client_money} FCFA, so your change is {change} FCFA.\n")
print("Thank you and enjoy your coffee! If you want something again, feel free to ask.")
