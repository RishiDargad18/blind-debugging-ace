def run(user, cmd):
    n = int(cmd)
    return n//3 if n % 3 == 0 else n*2 + 1

info = """[Problem 2]
Input: integer n
"""