# Write your solution here
L1 = input("1st letter: ")
L2 = input("2nd letter: ")
L3 = input("3rd letter: ")

if L1 > L2 and L1 < L3 or L1 > L3 and L1 < L2:
    print(f"The letter in the middle is {L1}")
elif L2 > L3 and L2 < L1 or L2 < L3 and L2 > L1:
    print(f"The letter in the middle is {L2}")
elif L3 > L1 and L3 < L2 or L3 < L1 and L3 > L2:
    print(f"The letter in the middle is {L3}")