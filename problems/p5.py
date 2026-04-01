def run(user, cmd):
    parts = cmd.split()
    
    s = parts[0]
    k = int(parts[1])

    n = len(s)
    res = [''] * n

    for i in range(n):
        if (i + k) % 2 == 0:
            j = (i + k) % n
        else:
            j = (i - k) % n

        if (i * j + k) % 3 == 0:
            j = (j + 2) % n

        res[i] = s[j]

    return "".join(res)


info = """Input:<string>~space~<integer>"""
