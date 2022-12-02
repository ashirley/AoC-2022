import sys

scores = {
  "X": 1,
  "Y": 2,
  "Z": 3,
  "A": 1,
  "B": 2,
  "C": 3,
}

totalScore = 0
for line in sys.stdin:
  them = line[0]
  you = line[2]

  score = scores[you]

  winner = (scores[you] - scores[them]) % 3
  if (winner == 0):
    score += 3
  elif (winner == 1):
    score += 6

  print(line[:-1], score)  
  totalScore += score

print(totalScore)   
