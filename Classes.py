import random


class lotterycard:
    """
    Класс, экзепляром которого является карточка для игры в лото. Каторчка состоит из трех рядов чисел
    """

    def __init__(self, name):
        self.sample1 = []
        self.sample2 = []
        self.sample3 = []
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.fullcard = []
        self.type = 'компьютер'
        self.name = name+' '+self.type

    def exclude_from_list(self,main_list, small_list):
        """
        Функция удаляет из основного списка значения, которые есть в другом списке
        :param main_list:
        :param small_list:
        :return: разница списков
        """
        main_list_set = set(main_list)
        small_list_set = set(small_list)
        new_set = main_list_set-small_list_set
        return list(new_set)


    def newcard(self):
        """
        Создание новой карточки путем последовательного случайного выбора 5 чисел для каждого ряда
        Также в каждый ряд случайным образом добавляются 4 пробела, чтобы общее число ячеек в ряду было 9
        :return:
        """
        all_numbers = [i for i in range(1,91)]
        self.sample1 = sorted(random.sample(all_numbers,5))
        numbers_excl_line1 = self.exclude_from_list(all_numbers,self.sample1)
        self.sample2 = sorted(random.sample(numbers_excl_line1,5))
        numbers_excl_line2 = self.exclude_from_list(numbers_excl_line1, self.sample2)
        self.sample3 = sorted(random.sample(numbers_excl_line2,5))
        self.line1= self.add_empty_cells(self.sample1)
        self.line2 = self.add_empty_cells(self.sample2)
        self.line3 = self.add_empty_cells(self.sample3)
        self.fullcard = self.line1+self.line2+self.line3

    def add_empty_cells(self, line):
        """
        Функция добавляет пробелы в список путем случайного выбора индекса элемента списка
        """
        cell_index = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        empty_cells = random.sample(cell_index, 4)
        result = list(line)
        for i in empty_cells:
            result.insert(i, "")
        return result

    # def makefullcard(self,list1,list2,list3):
    #     """
    #     функция возвращает общий список, состоящий из трех рядов карточки
    #     :param list1: ряд 1
    #     :param list2: ряд 2
    #     :param list3: ряд 3
    #     :return:
    #     """
    #     self.fullcard = list1+list2+list3

    # def makeset(self, list1):
    #     """
    #     создает множество значений, находящихся во всех рядах карточки (в трех списках)
    #     :return:
    #     """
    #     setofalllines = set(self.fullcard)
    #     return setofalllines

    def print_card(self,name):
        """
        Выводит на экран три ряда чисел в виде одной карточки
        :param name: имя игрока
        :return:
        """
        symbols = ["'", '[', ']', ]
        self.remove_symbols(self.fullcard,symbols)
        print("-"*3 + name, "-"*3 )
        print(self.fullcard[0:9])
        print(self.fullcard[9:18])
        print(self.fullcard[18:27])
        print("-" * 26)

    def replace_number(self,number, list):
        """
        Фукнция проверяет наличие числа в списке и зачеркивает его в случае совпадения
        :param number: число
        :param list: список чисел
        :return: список с замеченными числами
        """
        for i in range(len(list)):
            if list[i] == number:
                list[i] = "-"
        return list

    def remove_symbols(self,list, symbols):
        """
        Функция удаляет некоторые символы строки
        :param list:
        :param symbols:
        :return:
        """
        string = str(list)
        for i in string:
            if i in symbols:
                string = string.replace(i, "")
        return string

    def evaluate_response(self,barrel, list1):
        pass

    def find_winner(self, list1):
        """
        проверяет является ли пересечение множества чисел от 1 90 и множества чисел в карточке пустым или не пустым
        :return:
        """
        all_numbers = [i for i in range(1,91)]
        all_numbers_set = set(all_numbers)
        result = all_numbers_set&set(list1)
        return result == set()



class person_lotterycard(lotterycard):
    """
    Наследуемый класс для карточки, в случае если игроком является человек
    """
    def __init__(self, name):
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.fullcard = []
        self.type = 'пользователь'
        self.name = name + ' ' + self.type


    def evaluate_response(self, barrel, answer, list1):
        """
        Функция проверяет правильность ответвав игроков, которые являются людьми и прекращает игру в случае неверного ответа
        :param barrel:
        :return:
        """
        if answer == "y":
            if (barrel in set(list1))==True:
                print("Верно, номер зачеркнут")
                return True
            else:
                print("Неверный ответ. Номера нет Вы проиграли")
                return False

        elif answer == "n":
            if (barrel in set(list1))==False:
                print("верно")
                return True

            else:
                print("Неверный ответ. Номер есть Вы проиграли")
                return False





