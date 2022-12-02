import sys

scores = {
  "A": 1,
  "B": 2,
  "C": 3,
}

diff = {
  "X": -1,
  "Y": 0,
  "Z": 1
}

totalScore = 0
for line in sys.stdin:
  them = line[0]
  result = line[2]

  score = ((scores[them]-1 + diff[result]) % 3) + 1

  winner = diff[result]
  if (winner == 0):
    score += 3
  elif (winner == 1):
    score += 6

  print(line[:-1], score)  
  totalScore += score

print(totalScore)   
