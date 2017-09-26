import vk
from getpass import getpass


APP_ID = 6195469


def get_user_login():
    login = input("Please enter your login: ")
    return login


def get_user_password():
    password = getpass(prompt="Please enter your password: ")
    return password


def get_online_friends(login, password):
    user_list = []
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friend_list = api.friends.get(fields="online nickname")
    friends_online = [friend for friend in friend_list if friend["online"] == 1]
    return friends_online


def output_friends_to_console(friends_online):
    print("Online users: ")
    for idx, user in enumerate(friends_online, 1):
        print("{}) {} {}".format(idx, user["first_name"], user["last_name"]))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
