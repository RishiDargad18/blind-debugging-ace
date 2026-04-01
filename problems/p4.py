def run(user, cmd): 
    n = len(s)
    s = list(s)
    res = [''] * n

    # even indices → shift forward by 1
    evens = list(range(0, n, 2))
    for i in range(len(evens)):
        res[evens[i]] = s[evens[(i + 1) % len(evens)]]

    # odd indices → shift forward by 1 (same step, separate cycle)
    odds = list(range(1, n, 2))
    for i in range(len(odds)):
        res[odds[i]] = s[odds[(i + 1) % len(odds)]]

    return "".join(res)
info = """Input: String s"""
