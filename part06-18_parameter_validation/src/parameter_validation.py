# Write your solution here
def new_person(name: str, age: int):
  error = False
  if len(name) < 1 or len(name)>40:
    error = True
  elif len(name.split()) < 2:
    error = True
  elif age < 0 or age > 150:
    error = True
  
  if error:
    raise ValueError("something went wrong!")
  else:
    return (name, age)


if __name__=="__main__":
    name = input("Name: ")
    age = int(input("Age: "))
    person =  new_person(name, age)
    print(person)