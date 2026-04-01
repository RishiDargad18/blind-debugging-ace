def run(user, cmd):
    s = cmd.strip()
    n = len(s)

    s = list(s)
    res = [''] * n

    evens = list(range(0, n, 2))
    for i in range(len(evens)):
        res[evens[i]] = s[evens[(i + 1) % len(evens)]]

    odds = list(range(1, n, 2))
    for i in range(len(odds)):
        res[odds[i]] = s[odds[(i + 1) % len(odds)]]

    return "".join(res)
info = """Input: String s"""
