lines = open("input.txt").readlines()

previous_number = None
number_of_increases = 0

for line in lines:
  if previous_number is None:
    print(f"{line} (N/A)")
    previous_number = int(line)
    continue

  print(f"{line}", end="")

  if previous_number < int(line):
    print("(increased)")
    number_of_increases += 1
  else:
    print("(decreased)")
  
  previous_number = int(line)

print(number_of_increases)
