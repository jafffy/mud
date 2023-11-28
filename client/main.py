from mongoengine import *

import mud.context
from mud.commands.query import Stat
from mud.models.user import User


def main():
    connect('mud')

    context = mud.context.Context()
    commands = { Stat.command: Stat.do }

    username = input("username: ")

    user = User.objects(username=username).first()

    if user is None:
        raise f"User {username} not found"
    else:
        print(f"{username} 님, 접속을 환영합니다.")

        # Context initialization
        context.player_uuid = user.uuid

    while True:
        prompt = input("> ")

        if prompt == 'exit' or prompt == 'q' or prompt == 'quit':
            print("접속을 종료합니다.")
            break

        command = prompt.strip().split(" ")

        if command[0] not in commands:
            print("명령어를 찾을 수 없습니다.")
            continue

        commands[command[0]](context)


if __name__ == '__main__':
    main()
