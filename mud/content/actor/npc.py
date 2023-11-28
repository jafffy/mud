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

        print("1) 여긴 어디야?")
        print("2) 대화를 종료한다.")

        selection = int(input())

        if selection == 1:
            print("여긴 머드의 세계야. 일종의 시뮬레이션이지.")
        else:
            return


npc_map = {
    NPC_TALKER: Talker(name='토커')
}
