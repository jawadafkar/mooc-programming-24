# Write your solution here
def load_file(filename: str):
  list = []
  temp = []
  with open(filename) as recipes_file:
    for line in recipes_file:
      line = line.strip()
      if line != "":
        temp.append(line)
      else:
        list.append(temp)
        temp = []
    list.append(temp)
  return list


def search_by_name(filename: str, word: str):
  recipes = load_file(filename)
  
  list = []
  for item in recipes:
    if word in item[0].lower():
      list.append(item[0])
  return list

def search_by_time(filename: str, prep_time: int):
  recipes = load_file(filename)
  list = []
  for item in recipes:
    if int(item[1]) <= prep_time:
      list.append((f"{item[0]}, preparation time {item[1]} min" ))
  return list

def search_by_ingredient(filename: str, ingredient: str):
  recipes = load_file(filename)
  list = []
  for item in recipes:
    if ingredient in item:
      list.append((f"{item[0]}, preparation time {item[1]} min" ))
  return list


if __name__ == "__main__":
  found_recipes = search_by_name("recipes1.txt", "cake")
  found_recipes = search_by_time("recipes1.txt", 20)
  found_recipes = search_by_ingredient("recipes1.txt", "eggs")

  for recipe in found_recipes:
    print(recipe)
