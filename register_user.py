import uuid

from mongoengine import *

from mud.models.player import Player
from mud.models.user import User


def main():
    connect('mud')

    username = input("username: ")

    user = User.objects(username=username).first()
    if user is None:
        user = User(username=username)

        while True:
            uuid_value = str(uuid.uuid4())

            if User.objects(uuid=uuid_value).first() is None:
                user.uuid = uuid_value
                break

    print(user.uuid)
    user.save()


def on_user_created(user: User):
    player = Player.objects(uuid=user.uuid).first()
    if player is not None:
        raise f"duplicated player profile for the user {user.username}"

    player = Player(uuid=user.uuid)
    player.save()

    print(player.base_str, player.base_dex, player.base_int, player.base_will, player.base_luck)


if __name__ == '__main__':
    main()
