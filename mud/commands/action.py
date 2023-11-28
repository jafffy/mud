from mud.content.actor.npc import npc_map
from mud.content.place import place_map
from mud.context import Context


class Talk:
    command = 'talk'

    @staticmethod
    def do(context: Context, args: [str]):
        place = place_map[context.where]

        npc_idx = int(args[0]) - 1

        if npc_idx >= len(place.npcs):
            raise f"NPC #{npc_idx + 1} not found."

        npc_id = place.npcs[npc_idx]
        if npc_id not in npc_map.keys():
            raise f"NPC ID {npc_id} is not found."

        npc = npc_map[npc_id]
        npc.do(context)


class Move:
    command = 'move'

    @staticmethod
    def do(context: Context, args: [str]):
        place = place_map[context.where]

        idx_place_id_map = []

        i = 1
        for place_id in place.adjacent_places:
            idx_place_id_map.append((i, place_id))

        selection = 0

        if len(args) == 0:
            print("이동할 장소 (0은 이동하지 않음)")

            for pair in idx_place_id_map:
                print(f"{pair[0]}) {place_map[pair[1]].name}")

            selection = int(input())
        else:
            selection = int(args[0])

        if selection == 0:
            return

        for pair in idx_place_id_map:
            if selection == pair[0]:
                print(f"{place_map[pair[1]].name}로 이동")
                context.where = selection
                break
