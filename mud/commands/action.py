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
        print(f"{npc.name}: {npc.greeting}")
