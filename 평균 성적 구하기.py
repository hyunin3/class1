score = {
    'python': 80,
    'django': 89,
    'web': 83
}
score['algorithm'] = 90
score['python'] = 85
#print(score)
average_score = sum(score.values())/len(score)
print(average_score)