from mongoengine import Document, StringField


class Place(Document):
    uuid = StringField(required=True)
    name = StringField(required=True)