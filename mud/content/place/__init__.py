from mud.content.actor.npc import NPC_TALKER


class Place:
    def __init__(self, name, npcs):
        self.name = name
        self.npcs = npcs

STARTING_TOWN = 0

place_map = {
    STARTING_TOWN: Place('태초마을',
                         [NPC_TALKER])
}