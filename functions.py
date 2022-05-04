
def remove_symbols(list, symbols): #Функция удаляет некоторые символы строки
    string = str(list)
    for i in string:
        if i in symbols:
            string = string.replace(i,"")
    return string

def get_number():
    while True:
        number_of_players = input("Введите количество игроков ")
        if number_of_players.isdigit()==True:
            return int(number_of_players)
        else:
            print("Неправильно введено количество игроков")

def get_type_of_player(player):
    while True:
        type_of_player = input("Выберете тип " + player + ': "1" - человек, "2" - компьютер ')
        if type_of_player=="1" or "2":
            return type_of_player
        else:
            print("Неправильно указан тип игрока")