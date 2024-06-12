# Write your solution here
def oldest_person(people: list):
  oldest_age = people[0][1]
  oldest_name = people[0][0]
  for tuple in people:
    if tuple[1] < oldest_age:
      oldest_age = tuple[1]
      oldest_name = tuple[0]
  return oldest_name
  
if __name__ == "__main__":
  p1 = ("Adam", 1977)
  p2 = ("Ellen", 1985)
  p3 = ("Mary", 1953)
  p4 = ("Ernest", 1997)
  people = [p1, p2, p3, p4]

  print(oldest_person(people))