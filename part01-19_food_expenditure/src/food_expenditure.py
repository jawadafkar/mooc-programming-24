# Write your solution here
eat = int(input("How many time s a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
avg_sp = float(input("How much money do you spend on groceries in a week? "))
week = 7
total = eat * price + avg_sp
daily = total / week
print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {total} euros")