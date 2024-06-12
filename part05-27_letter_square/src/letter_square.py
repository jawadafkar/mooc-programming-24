a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

layer = int(input("Layers: "))
p = layer + layer - 1
col = p
l = layer-1
row = 0
right = 0
left = layer

while row < layer:
  line = ""
  for i in range(layer-1, layer - right-1, -1):
    line += a[i]
  
  right += 1

  line += f"{a[l]*p}"
  row += 1
  p -= 2
  l -= 1

  for i in range(left, layer):
    line += a[i]
  left -= 1

  print(line)

right -= 2
left += 2
l += 2
p += 4

while row < col:
  line = ""
  
  for i in range(layer-1, layer - right - 1, -1):
    line += a[i]
  right -= 1

  line += f"{a[l]*p}"
  row += 1
  p += 2
  l += 1  
  
  
  for i in range(left, layer):
    line += a[i]
  left += 1
  print(line)