import json


tariff = 50
days_cnt = 2
current_user = 1
default_user_id = 1

def get_users():
    with open('users.json') as f:
        users = json.load(f)
        return users


users = get_users()
