lines = open("input.txt").readlines()

x = 0
y = 0
z = 0
for l in lines:
  if l.startswith("forward"):
    x += int(l.strip("forward").strip())
    y += int(l.strip("forward").strip()) * z
  elif l.startswith("up"):
    z += int(l.strip("up").strip())
  elif l.startswith("down"):
    z -= int(l.strip("down").strip())

print(f"part 1: {x*z/-1}")
print(f"part 2: {x*y/-1}")
