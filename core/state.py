users = {}

def get_user(uid):
    if uid not in users:
        users[uid] = {
            "problem": 1,
            "data": {}
        }
    return users[uid]