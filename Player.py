import random
class Player:
    def __init__(self, name, current_hp, max_hp, current_mp, max_mp, credit, attack, initiative, defense, spell_list, items,fight_state):
        self.name = name
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.current_mp = current_mp
        self.max_mp = max_mp
        self.credit = credit
        self.attack = attack
        self.initiative = initiative
        self.defense = defense
        self.spell_list = spell_list
        self.items = items
        self.fight_state = fight_state

    def generate_damage(self, attack):
        attack_range = random.randrange(0, 2, 1)
        return attack + attack_range

    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp <= 0:
            print("You died!")

    def get_hp(self, amount):
        self.current_hp += amount


