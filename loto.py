
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
import sys
from Classes import lotterycard, user_player, computer_player


number_of_players = None
while True:
    request = input("Введите количество игроков ")
    if request.isdigit() == True:
        number_of_players= int(request)
        break
    else:
        print("Неправильно введено количество игроков. Повторите ввод")

players_list = []
for i in range(0,number_of_players):
    while True:
        name = "Игрок №"+str(i+1)
        choice_of_player = input("Выберете тип " + name + ': "1" - человек, "2" - компьютер ')
        if choice_of_player in ["1","2"]:
            break
        else:
            print("Неправильный ввод")
    player = user_player(name) if choice_of_player == "1" else computer_player(name)
    players_list.append(player)

emptycardlist = [lotterycard(i.name, i.type) for i in players_list]
cardlist = []
for card in emptycardlist:
    card.newcard()
    cardlist.append(card)

all_barrels = [i for i in range(1, 91)]
random.shuffle(all_barrels)
for i in all_barrels:
    print("Номер бочонка ", i)
    for card in cardlist:
         print(card)
         if card.type == "человек":
            while True:
                answer = input('Есть ли в вашей карточке такой номер (если да, нажмите "y"/ если нет, нажмите "n")? ')
                if answer in ["y","n"]:
                    if card.evaluate_response(i,answer, card.fullcard)==True:
                        card.replace_number(i, card.fullcard)
                        break
                    else:
                        sys.exit()
                else:
                    print("Incorrect input")
         else:
             card.replace_number(i, card.fullcard)
         if card.find_winner(card.fullcard)==True:
            print("Победителем стал ", card.name)
            sys.exit()

