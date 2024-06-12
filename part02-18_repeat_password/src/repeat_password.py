# Write your solution here

password = input("Password: ")

while True:
    repass = input("Repeat password: ")

    if password == repass:
        print("User account created!")
        break
    else:
        print("They do not match!")
