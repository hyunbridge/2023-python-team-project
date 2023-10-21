# Exercise 12

quiz = []
quiz.append('1.중국의 수도를 선택하세요./1)칭따오/2)상하이/3)베이징/3')
quiz.append('2.인도의 수도를 선택하세요./1)시라즈/2)뉴델리/3)이스파한/2')
quiz.append('3.태의 수도를 선택하세요./1)칸깬/2)방콕/3)핫야이/2')

for question in quiz:
    print(question)
    answer = input('-->답을 선택하세요:')

    if answer == question.split('/')[4]:
        print('-->정답입니다.!\n')
    else:
        print('-->오답입니다.!\n')
