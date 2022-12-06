import sys, re
count = 0

for line in sys.stdin:
  m = re.search(r"([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)", line)
  start1 = int(m.group(1))
  stop1 = int(m.group(2))
  start2 = int(m.group(3))
  stop2 = int(m.group(4))

  if (start1 <= start2 and stop1 >= start2):
    #1 covers 2
    count += 1
    print("1", line[:-1], start1, stop1, start2, stop2)
  elif (start2 <= start1 and stop2 >= start1):
    #2 covers 1
    count += 1
    print("2", line[:-1], start1, stop1, start2, stop2)
  else:
    pass
    print(" ", line[:-1], start1, stop1, start2, stop2)

print(count)   
