from mud.context import Context
from mud.models.player import Player


class Stat:
    command = 'stat'

    @staticmethod
    def do(context: Context):
        player = Player.objects(uuid=context.uuid).first()

        if player is None:
            raise f"Player uuid ({context.uuid}) not found."

        print(f"힘: {player.base_str}")
        print(f"솜씨: {player.base_dex}")
        print(f"지력: {player.base_int}")
        print(f"의지: {player.base_will}")
        print(f"행운: {player.base_luck}")
