# Write your solution here
editor = ""
while editor.lower() != "visual studio code":
    editor = input("Editor: ")
    if editor.lower() == "visual studio code":
        print("an excellent choice!")
    elif editor.lower() == "word":
        print("awful")
    else:
        print("not good")
