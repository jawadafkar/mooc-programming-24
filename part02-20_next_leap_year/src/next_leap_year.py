# Write your solution here
year = int(input("Year: "))
n = year
while True:
    n += 1
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print(f"The next leap year after {year} is {n}")
        break