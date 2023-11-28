from mud.content import PLACE_STARTING_TOWN, NPC_TALKER, PLACE_HUNTING_PLACE


class Place:
    def __init__(self, name, npcs, adjacent_places):
        self.name = name
        self.npcs = npcs
        self.adjacent_places = adjacent_places


place_map = {
    PLACE_STARTING_TOWN: Place('태초마을',
                               [NPC_TALKER],
                               [PLACE_HUNTING_PLACE]),
    PLACE_HUNTING_PLACE: Place('사냥터',
                               [],
                               [PLACE_STARTING_TOWN]),
}
