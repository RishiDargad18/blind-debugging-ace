def run(user, cmd):
    n = int(cmd)
    return n*n + sum(map(int, str(n)))

info = """Input: integer n"""