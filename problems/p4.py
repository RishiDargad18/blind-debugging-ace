def run(user, cmd):
    if "count" not in user:
        user["count"] = 0

    user["count"] += 1
    return int(cmd) * user["count"]

info = """Problem 4:
Input: integer n
"""