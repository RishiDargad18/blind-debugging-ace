def run(user, cmd):
    if "queue" not in user:
        user["queue"] = []

    parts = cmd.split()

    if parts[0] == "push":
        user["queue"].append(int(parts[1]))
        return "ok"

    elif parts[0] == "pop":
        if user["queue"]:
            return user["queue"].pop(0)
        return "empty"

    elif parts[0] == "top":
        return user["queue"][0] if user["queue"] else "empty"

    return "invalid command"

info = """Problem 5:
Commands:
push x
pop
top
"""