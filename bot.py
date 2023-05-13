def bot_introduce(name, age):
    return f"Hello my name is {name}.\nI was created in {age}."

def user_name():
    print("Please, remind me your name.")
    _name = input()
    return f"What a great name you have, {_name}!"

def guess_age(rem3, rem5, rem7):
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    return f"Your age is {age}; that's a good time to start programming!"

print(bot_introduce("OniGiri", 2023))
print(user_name())
print("Let me guess your age.\nEnter reminders of dividing your age by 3, 5 and 7")
print(guess_age(int(input()), int(input()), int(input())))
