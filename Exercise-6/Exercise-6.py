odd = 0
even = 0

for i in range(1, 101):
    if (i % 2):
        odd += i
    else:
        even += i

print('홀수의 합 :', odd)
print('짝수의 합 :', even)
