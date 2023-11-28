from mud.content.place import STARTING_TOWN


class Context:
    def __init__(self, uuid=''):
        self.player_uuid = uuid
        self.where = STARTING_TOWN
