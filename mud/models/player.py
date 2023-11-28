from mongoengine import Document, StringField, IntField


class Player(Document):
    uuid = StringField(required=True)

    base_str = IntField(required=True, default=0)
    base_dex = IntField(required=True, default=0)
    base_int = IntField(required=True, default=0)
    base_will = IntField(required=True, default=0)
    base_luck = IntField(required=True, default=0)

    money = IntField(required=True, default=0)
