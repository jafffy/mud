from datetime import datetime

from mud.content.actor.npc import npc_map
from mud.content.place import place_map
from mud.context import Context
from mud.models.player import Player


class Stat:
    command = 'stat'

    @staticmethod
    def do(context: Context, args: [str]):
        player = Player.objects(uuid=context.player_uuid).first()

        if player is None:
            raise f"Player uuid ({context.player_uuid}) not found."

        print(f"힘: {player.base_str}")
        print(f"솜씨: {player.base_dex}")
        print(f"지력: {player.base_int}")
        print(f"의지: {player.base_will}")
        print(f"행운: {player.base_luck}")
        print(f"\n경험치: {player.exp}")


class Where:
    command = 'where'

    @staticmethod
    def do(context: Context, args: [str]):
        current_place = place_map[context.where]

        print(f"현재 위치: {current_place.name}")

        print(f"현재 위치의 NPC ({len(current_place.npcs)} 명)")

        i = 1
        for npc_id in current_place.npcs:
            print(f"{i}) {npc_map[npc_id].name}")
            i += 1


class Time:
    command = 'time'

    @staticmethod
    def do(context: Context, args: [str]):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
