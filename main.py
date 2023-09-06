
import Player
from Utility import *
import Enemy

spieler = Player.Player("", 200, 100, 100, 100, 0, 10, 10,2, [], [], False)
spieler.name = input("Wie lautet Dein Name?\n> ")
choose_first_spell(spieler)

first_enemy = Enemy.Enemy("Goblin", 100, 100, 10, 5)


game_state = True
counter = 100
while game_state:
    print("Du hast noch: " + str(counter) + " Züge")

    choose_next_step(spieler,  first_enemy)
    counter -= 1
    if counter == 0:
        game_state = False
        print("Du hast das Spiel Überlebt!")
