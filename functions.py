
def remove_symbols(list, symbols):
    """
    Функция удаляет некоторые символы строки
    :param list:
    :param symbols:
    :return:
    """
    string = str(list)
    for i in string:
        if i in symbols:
            string = string.replace(i,"")
    return string

def get_number():
    """
    Функция проверяет, что введенное количество игроков является числом. В ином случае предлагается повторить ввод
    :return:
    """
    while True:
        number_of_players = input("Введите количество игроков ")
        if number_of_players.isdigit()==True:
            return int(number_of_players)
        else:
            print("Неправильно введено количество игроков. Повторите ввод")

def get_type_of_player(player):
    """
    Функция проверяет корректный ввод для выбора типа игрока. В случае неправильного ввода, предлагается повторить ввод.
    :param player:
    :return:
    """
    while True:
        type_of_player = input("Выберете тип " + player + ': "1" - человек, "2" - компьютер ')
        if type_of_player in ["1","2"]:
            return type_of_player
        else:
            print("Неправильно указан тип игрока. Повторите ввод")


