# Write your solution here
def factorials(n: int):
  factorial = {}
  mul = 1
  for i in range(1, n+1):
    mul *= i
    factorial[i] = mul
  return factorial


if __name__ == "__main__":
  k = factorials(5)
  print(k[1])
  print(k[3])
  print(k[5])