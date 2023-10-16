# Exercise 8

for i in range(1, 101):
    isDivisibleBy3 = i % 3 == 0
    isDivisibleBy5 = i % 5 == 0

    if isDivisibleBy3:
        print("Fizz", end="")
    if isDivisibleBy5:
        print("Buzz", end="")
    
    if not isDivisibleBy3 and not isDivisibleBy5:
        print(i, end="")
    
    print()
