def run(user, cmd):
    s = cmd
    res = ""

    for c in s:
        if c.isalpha():
            res += chr((ord(c)-97+2)%26 + 97)
        else:
            res += c

    return res[::-1]

info = """Problem 3:
Input: lowercase string

Example: abc
"""