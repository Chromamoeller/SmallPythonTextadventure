import random
import Spell

def choose_next_step(spieler, enemy):
    player_choice = input(
        "**********Hauptmenu**********\n"
        "Was möchtest Du tun?\n1: Vorwärts\n2: Links\n3: Rechts\n4: Zurück\n> ")
    if player_choice == "1":
        print("Du gehst vorwärts.")
        random.choice([chance_for_encounter_enemy(spieler, enemy),
                      chance_for_encounter_tressure()])
    elif player_choice == "2":
        print("Du gehst nach links.")
        random.choice([chance_for_encounter_enemy(spieler, enemy),
                      chance_for_encounter_tressure()])
    elif player_choice == "3":
        print("Du gehst nach rechts.")
        random.choice([chance_for_encounter_enemy(spieler, enemy),
                      chance_for_encounter_tressure()])
    elif player_choice == "4":
        print("Du gehst zurück.")
        random.choice([chance_for_encounter_enemy(spieler, enemy),
                      chance_for_encounter_tressure()])
    else:
        print("Bitte wähle eine der Optionen aus.")
        choose_next_step(spieler, enemy)


def encounter_enemy(spieler, enemy):
    print("Du triffst auf einen Gegner!")
    player_choice = input("Was möchtest Du tun?\n1: Kämpfen\n 2: Fliehen\n > ")
    if player_choice == "1":
        print("Du greifst an.")
        fight(spieler, enemy)
    elif player_choice == "2":
        print("Du versuchst zu fliehen.")
    else:
        print("Bitte wähle eine der Optionen aus.")
        encounter_enemy(spieler, enemy)


def encounter_treasure():
    print("Du findest einen Schatz!")
    player_choice = input(
        "Was möchtest Du tun?\n1: Öffnen\n2: Weitergehen\n> ")
    if player_choice == "1":
        print("Du öffnest den Schatz.")
    elif player_choice == "2":
        print("Du gehst weiter.")
    else:
        print("Bitte wähle eine der Optionen aus.")
        encounter_treasure()

def choose_first_spell(spieler):
    choosen_spell = input("Welchen Zauber möchtest Du wählen?\n1: Feuerball\n2: Frostschock\n3: Blitzschlag\n> ")
    if choosen_spell == "1":
        spieler.spell_list.append(Spell.all_fire_spells[0])
        print("Du hast einen neuen Zauber erlernt: " + Spell.all_fire_spells[0].name + "\n")
    elif choosen_spell == "2":
        spieler.spell_list.append(Spell.all_ice_spells[0])
        print("Du hast einen neuen Zauber erlernt: " + Spell.all_ice_spells[0].name + "\n")
    elif choosen_spell == "3":
        spieler.spell_list.append(Spell.all_lightning_spells[0])
        print("Du hast einen neuen Zauber erlernt: " + Spell.all_lightning_spells[0].name + "\n")
    else:
        print("Bitte wähle einen Zauber aus.")
        choose_first_spell(spieler)

def chance_for_encounter_enemy(spieler, enemy):
    encounter_chance = random.randrange(0, 2, 1)
    if encounter_chance == 0:
        encounter_enemy(spieler, enemy)


def chance_for_encounter_tressure():
    encounter_chance = random.randrange(0, 6, 1)
    if encounter_chance == 0:
        encounter_treasure()


def fight(spieler, enemy):
    spieler.fight_state = True
    print("******* Fight *******")
    while spieler.fight_state:
        player_choice = input(
            "Was möchtest Du tun?\n1: Nahkampfangreiff\n2: Zauber Wirken\n> ")
        if player_choice == "1":
            calc_init(spieler, enemy, spieler.attack)
            print(spieler.name)
        elif player_choice == "2":
            print("Zauber wirken")
        else:
            print("Bitte wähle eine der Optionen aus.")
            fight(spieler, enemy)


def choose_spell(spieler, gegner):
    print("Welchen Zauber möchtest Du wirken?")
    for spell in spieler.spell_list:
        print("> " + spell.name)
    choosen_spell = input("> ")


def calc_init(spieler, gegner):
    if spieler.initiative > gegner.initiative:
        calc_damage(spieler, gegner)
    else:
        calc_damage(gegner, spieler)


def calc_damage(init_winner, init_looser):
    init_looser.current_hp -= init_winner.attack
    print(init_looser.name + " hat noch " + str(init_looser.current_hp) + " HP.")
    init_winner.current_hp -= init_looser.attack
    print(init_winner.name + " hat noch " + str(init_winner.current_hp) + " HP.")
    check_life(init_winner, init_looser)

def check_life(spieler, gegner):
    if spieler.current_hp <= 0:
        print("Du bist tot!")
        spieler.fight_state = True
    elif gegner.current_hp <= 0:
        print("Der Gegner ist tot!")
        spieler.fight_state = False

