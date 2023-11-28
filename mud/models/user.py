from mongoengine import Document, StringField


class User(Document):
    username = StringField(required=True)
    uuid = StringField(required=False)