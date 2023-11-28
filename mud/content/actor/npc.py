from mud.content import NPC_TALKER
from mud.context import Context
from mud.models.player import Player


class NPC:
    def __init__(self, name):
        self.name = name

    def do(self, context: Context):
        pass


class Talker(NPC):
    def do(self, context: Context):
        player = Player.objects(uuid=context.player_uuid).first()
        if player is None:
            raise f"Player UUID {context.player_uuid} not found"

        print(f"안녕, {player.name}. 난 토커라고 해!")


npc_map = {
    NPC_TALKER: Talker(name='토커')
}