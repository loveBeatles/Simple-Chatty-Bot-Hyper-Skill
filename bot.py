def bot_introduce(name, age):
    return f"Hello my name is {name}.\nI was created in {age}."

def user_name():
    print("Please, remind me your name.")
    _name = input()
    return f"What a great name you have, {_name}!"

print(bot_introduce("OniGiri", 2023))
print(user_name())