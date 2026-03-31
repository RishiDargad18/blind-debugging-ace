users = {}

def get_user(uid):
    if uid not in users:
        users[uid] = {
            "problem": None,
            "data": {}
        }
    return users[uid]
