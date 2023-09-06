
class Spell:
    def __init__(self, name, cost, damage, type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type

    def __str__(self):
        return f"{self.name} costs {self.cost} and does {self.damage} damage of type {self.type}"



all_spells = []
all_fire_spells = []
all_ice_spells = []
all_lightning_spells = []

fireball = Spell("Fireball", 10, 100, "fire")
all_fire_spells.append(fireball)

frost_shock = Spell("Frost Shock", 10, 100, "ice")
all_ice_spells.append(frost_shock)
lightning_bolt = Spell("Lightning Bolt", 10, 100, "lightning")
all_lightning_spells.append(lightning_bolt)

all_spells.append(all_fire_spells)
all_spells.append(all_ice_spells)
all_spells.append(all_lightning_spells)

