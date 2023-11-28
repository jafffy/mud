class NPC:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting

NPC_TALKER = 0

npc_map = {
    NPC_TALKER: NPC(name='토커', greeting="안녕, 난 토커라고 해!")
}