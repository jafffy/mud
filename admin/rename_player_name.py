import uuid

from mongoengine import *

from mud.models.player import Player
from mud.models.user import User


def main():
    connect('mud')

    username = input("username: ")

    user = User.objects(username=username).first()
    if user is None:
        raise f"Username {username} is not found."

    player = Player.objects(uuid=user.uuid).first()
    player.name = input("캐릭터의 이름을 입력하세요: ")

    player.save()


if __name__ == '__main__':
    main()
