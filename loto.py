import random
from Classes import lotterycard, person_lotterycard
from functions import get_number, get_type_of_player

name = "Игрок"
number_of_players = get_number()
players_list = []
for i in range(0,number_of_players):
    players_list.append(name+" №"+str(i+1))

players_cardlist = []
for player in players_list:
    #player_choice = input("Выберете тип " + player + ": 1- человек, другое значение - компьютер ")
    player_choice = get_type_of_player(player)
    player = person_lotterycard(player) if player_choice == "1" else lotterycard(player)
    player.newcard()
    players_cardlist.append(player)


all_barrels = [i for i in range(1, 91)]
random.shuffle(all_barrels)
for i in all_barrels:
    print("Номер бочонка ", i)
    for player in players_cardlist:
        player.print_card(player.name)
        player.сrossout_number(i)
        player.find_winner()
