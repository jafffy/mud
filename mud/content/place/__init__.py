from mud.content import STARTING_TOWN, NPC_TALKER


class Place:
    def __init__(self, name, npcs):
        self.name = name
        self.npcs = npcs

place_map = {
    STARTING_TOWN: Place('태초마을',
                         [NPC_TALKER])
}