# Exercise-3
age = int(input('나이를 입력하세요: '))
balance = 5000
if 8 <= age <= 12 :
    balance -= 650
elif 13 <= age <= 18 :
    balance -= 1050
elif 19 <= age <= 59 :
    balance -= 1250
print('잔액 = ', balance)
