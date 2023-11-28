from mongoengine import *
from mud.models.user import User


def main():
    connect('mud')

    username = input("username: ")

    user = User.objects(username=username).first()

    if user is None:
        raise f"User {username} not found"
    else:
        print(f"{username} 님, 접속을 환영합니다.")

    while True:
        prompt = input("> ")

        if prompt == 'exit' or prompt == 'q' or prompt == 'quit':
            print("접속을 종료합니다.")
            break

        command = prompt.strip().split(" ")

        print(command)


if __name__ == '__main__':
    main()
