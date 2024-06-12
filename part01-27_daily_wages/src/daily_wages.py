# Write your solution here

wage = float(input("Hourly wage: "))
hour = int(input("Hours worked: "))
day = input("Day of the week: ")

sunday = day == "Sunday"
salary = wage * hour
if sunday:
    salary = wage * hour * 2

print(f"Daily wages: {salary} euros")