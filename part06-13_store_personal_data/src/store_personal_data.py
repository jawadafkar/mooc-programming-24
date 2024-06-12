# Write your solution here
def store_personal_data(person: tuple):
  with open("people.csv", "a") as file:
    file.write(person[0] + ";" + str(person[1]) + ";" + str(person[2]) + "\n")

if __name__ == "__main__":
  store_personal_data(("Jawad Afkar", 26, 178.5))