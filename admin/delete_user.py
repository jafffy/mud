import uuid

from mongoengine import *
from mud.models.user import User


def main():
    connect('mud')

    username = input("username: ")

    user = User.objects(username=username).first()
    user.delete()


if __name__ == '__main__':
    main()
