def bot_introduce(name, age):
    return f"Hello my name is {name}.\nI was created in {age}."

def user_name():
    print("Please, remind me your name.")
    _name = input()
    return f"What a great name you have, {_name}!"

def guess_age(rem3, rem5, rem7):
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    return f"Your age is {age}; that's a good time to start programming!"

def count_to_number(number):
    for i in range(number + 1):
        print(i, "!")
    return "Completed, have a nice day!"

def programming_knowledge():
    print("""Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
    select = int(input())
    while select != 2:
        print("Please, try again.")
        select = int(input())
    else:
        return "Congratulations, have a nice day!"

print(bot_introduce("OniGiri", 2023))
print(user_name())
print("Let me guess your age.\nEnter reminders of dividing your age by 3, 5 and 7")
print(guess_age(int(input()), int(input()), int(input())))
print("Now I will prove to you that I can count to any number you want.")
print(count_to_number(int(input())))
print(programming_knowledge())