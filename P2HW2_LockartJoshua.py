# CTI-110
# P2HW2 - Score Avg
# Joshua Lockart
# 2/25/20222
#

#assigning variables via input function
score_1 = float(input('Enter score'))
score_2 = float(input('Enter score'))
score_3 = float(input('Enter score'))
score_4 = float(input('Enter score'))
score_5 = float(input('Enter score'))
score_6 = float(input('Enter score'))
score_7 = float(input('Enter score'))

#making a list for all scores input
scores = [score_1, score_2, score_3, score_4, score_5, score_6, score_7]

#printing the output with some calculations mixed in
print('Lowest Score:', min(scores))
scores.remove(min(scores))
print('Modified List:', scores)
print('Scores Average:{:.2f}'.format(sum(scores) / len(scores)))