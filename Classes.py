import random
import sys
from functions import remove_symbols


class lotterycard:
    """
    Класс, экзепляром которого является карточка для игры в лото. Каторчка состоит из трех рядов чисел
    """

    def __init__(self, name):
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.fullcard = []
        self.name = name+' компьютер'

    def newcard(self):
        """
        Создание новой карточки путем последовательного случайного выбора 5 чисел для каждого ряда
        Также в каждый ряд случайным образом добавляются 4 пробела, чтобы общее число ячеек в ряду было 9
        :return:
        """
        all_numbers = [i for i in range(1,91)]
        all_numbers_set = set(all_numbers)
        line1 = sorted(random.sample(all_numbers,5))
        line1_set = set(line1)
        numbers_excl_line1_set = all_numbers_set-line1_set
        numbers_excl_line1 = list(numbers_excl_line1_set)
        line2 = sorted(random.sample(numbers_excl_line1,5))
        line2_set = set(line2)
        numbers_excl_lines1and2_set = numbers_excl_line1_set-line2_set
        numbers_excl_lines1and2 = list(numbers_excl_lines1and2_set)
        line3 = sorted(random.sample(numbers_excl_lines1and2,5))
        self.line1= self.add_empty_cells(line1)
        self.line2 = self.add_empty_cells(line2)
        self.line3 = self.add_empty_cells(line3)

    def add_empty_cells(self, line):
        """
        Функция добавляет пробелы в список путем случайного выбора индекса элемента списка
        """
        cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        empty_cells = random.sample(cells, 4)
        for i in empty_cells:
            line.insert(i, "")
        return line

    def makeset(self):
        """
        создает множество чисел, находящихся во всех рядах карточки
        :return:
        """
        setoflines = set(self.line1 + self.line2 + self.line3)
        return setoflines

    def print_card(self,name):
        """
        Выводит на экран три ряда чисел в виде одной карточки
        :param name: имя игрока
        :return:
        """
        print("-"*3 + name, "-"*3 )
        symbols = ["'",'[',']',]
        print(remove_symbols(self.line1,symbols))
        print(remove_symbols(self.line2, symbols))
        print(remove_symbols(self.line3, symbols))
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

    def сrossout_number(self,barrel):
        """
        проверяет ряды карточки и зачеркивает номер карточки, заменяет цифру на знак "-"
        :param barrel:
        :return:
        """
        self.line1 = self.replace_number(barrel, self.line1)
        self.line2 = self.replace_number(barrel, self.line2)
        self.line3 = self.replace_number(barrel, self.line3)
        # self.line2 = cross_number(barrel, self.line2)
        # self.line3 = cross_number(barrel, self.line3)

    def find_winner(self):
        """
        проверяет является ли пересечение множества чисел от 1 90 и множества чисел в карточке пустым или не пустым
        если пересечение пустое, то это означает, что в карточке зачеркнуты все числа и игра заканчивается
        :return:
        """
        all_numbers = [i for i in range(1,91)]
        all_numbers_set = set(all_numbers)
        result = all_numbers_set&self.makeset()
        if result == set():
            print("Победителем стал ",self.name )
            sys.exit()


class person_lotterycard(lotterycard):
    """
    Наследуемый класс для карточки, в случае если игроком является человек
    """

    def __init__(self, name):
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.fullcard = []
        self.name = name+' пользователь'
        self.numbersincardlist = []
        self.numbersincard = {}

    def сrossout_number(self,barrel):
        """
        Функция проверяет правильность ответвав игроков, которые являются людьми и зачеркивает совпавшие номера, если игрок
        правильно ответил, что номер выпавшего бочонка есть в его карточке
        """
        answer = input('Есть ли в вашей карточке такой номер (если да, нажмите "y"/ если нет, нажмите "n")? ')
        if answer == "y":
            if (barrel in self.makeset())==True:
                self.line1 = self.replace_number(barrel, self.line1)
                self.line2 = self.replace_number(barrel, self.line2)
                self.line3 = self.replace_number(barrel, self.line3)
                print("Верно, номер зачеркнут")
            else:
                 print("Неверный ответ. Номера нет Вы проиграли")
                 sys.exit()
        elif answer == "n":
             if (barrel in self.makeset())==False:
                 print("верно")
             else:
                 print("Неверный ответ. Номер есть Вы проиграли")
                 sys.exit()
        else:
             print("неправильный ввод")


