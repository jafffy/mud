from mud.content.place import PLACE_STARTING_TOWN


class Context:
    def __init__(self, uuid=''):
        self.player_uuid = uuid
        self.where = PLACE_STARTING_TOWN
