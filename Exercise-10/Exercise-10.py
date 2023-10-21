# Exercise 10

score = []

for i in range(1,11):
    val = int(input('{}. 점수를 입력하세요: '.format(i)))
    score.append(val)

total = sum(score)
result = total / len(score)
    
print('평균: {}'.format(result))
