import random

print("Welcome to the Simple Multiplication Quiz!")
print("You will be given 5 multiplication problems to solve.")

correct_count = 0
incorrect_count = 0

for i in range(1, 6):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    print(f"Problem {i}: What is {num1} x {num2}?")


    multiply = num1 * num2

    answer = int(input("Your answer: "))
    print("Your answer:" + str(answer))

    def is_equal(a, b):
        return a == b

    if is_equal(answer, multiply):
        print("Correct!")
        correct_count += 1 
    else:
        print(f"Incorrect. The correct answer was {multiply}.")
        incorrect_count += 1 

total_count = correct_count + incorrect_count        

print(f"You scored {correct_count} out of {total_count}. Well done!")
