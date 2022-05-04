
"""
Игра Лото

Правила игры.

Игра состоит из специальных карточек на которых отмечены числа и бочонков с цифрами

Всего 90 бочонков с цифрами от 1 до 90 (В жизни они обычно достаются из мешка чтобы можно было вытянуть случайно)

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Так выглядит пример карточки:

В игре любое количество игроков двух типов: пользователь и компьютер. Каждому в начале выдается случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточки игроков

Игрокам - пользователям предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Компьютер всегда правильно зачеркивает свои цифры если они есть и продолжает если их нет

Побеждает тот, кто первый закроет все числа на своей карточке.

"""



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
