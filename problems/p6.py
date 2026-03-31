import random

def run(user, cmd):
    if "num" not in user:
        user["num"] = random.randint(1, 1000)

    guess = int(cmd)
    num = user["num"]

    if guess < num:
        return "too low"
    elif guess > num:
        return "too high"
    else:
        return "correct"

info = """Problem 6:
Guess a number between 1 and 1000
"""