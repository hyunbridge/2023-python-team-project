# Exercise 9

STANDARD = 70
score = [70, 60, 55, 75, 95, 90, 80, 65, 85, 100]

count = 0

for i in score:
    if i < STANDARD:
        count += 1

print(f"{STANDARD}점 미만인 학생의 수 : {count}")