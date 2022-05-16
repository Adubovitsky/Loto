import unittest
from Classes import lotterycard, person_lotterycard

class Test_lotterycard(unittest.TestCase):
    def test_init(self):
        card = lotterycard("Player")
        self.assertEqual(card.line1,[])
        self.assertEqual(card.line2, [])
        self.assertEqual(card.line3, [])
        self.assertEqual(card.fullcard, [])
        self.assertEqual(card.name, "Player компьютер")

    def test_exludefromlist(self):
        card = lotterycard("Player")
        main_list = [1,2,3,4,5,6,7,8,10]
        small_list = [2,3,4]
        self.assertEqual(card.exclude_from_list(main_list,small_list),[1,5,6,7,8,10])

    def test_newcard(self):
        card = lotterycard("Player")
        card.newcard()
        self.assertEqual(len(card.line1), 9)
        self.assertEqual(len(card.line2), 9)
        self.assertEqual(len(card.line3), 9)
        self.assertEqual(len(card.sample1), 5)
        self.assertEqual(len(card.sample2), 5)
        self.assertEqual(len(card.sample3), 5)
        self.assertEqual(set(card.line1) & set(card.line2) & set(card.line3), {""})
        self.assertEqual(len(set(card.sample1).union(set(card.sample2), set(card.sample3))), 15)
        for i in range(5):
            self.assertGreaterEqual(int(card.sample1[i]),1)
            self.assertGreaterEqual(int(card.sample2[i]), 1)
            self.assertGreaterEqual(int(card.sample3[i]), 1)
            self.assertLessEqual(int(card.sample1[i]), 91)
            self.assertLessEqual(int(card.sample2[i]), 91)
            self.assertLessEqual(int(card.sample3[i]), 91)

    def test_addemptycells(self):
        card = lotterycard("Player")
        my_list = [3,12,27,100]
        self.assertEqual(len(card.add_empty_cells(my_list)),8)
        self.assertEqual(len(set(card.add_empty_cells(my_list))), 5)

    def test_replacenumber(self):
        card = lotterycard("Player")
        number = 10
        list_1 = [1,3,7,10]
        self.assertNotIn(number,card.replace_number(number,list_1))

    def test_findwinner(self):
        card = lotterycard("Player")
        list1 = [0,92,101]
        self.assertTrue(card.find_winner(list1),set())
        list1 = [0, 90, 101]
        self.assertFalse(card.find_winner(list1), set())

    def test_evaluateresponse(self):
        card = person_lotterycard("Player")
        list1 = [1, 32, 11,45,56]
        answer1 = "y"
        barrel1 = 1
        self.assertTrue(card.evaluate_response(barrel1,answer1,list1))
        list4 = [1, 32, 11,45,56]
        answer2 = "n"
        barrel2 = 1
        self.assertFalse(card.evaluate_response(barrel2,answer2,list4))
        list7 = [1, 32, 11, 45, 56]
        answer3 = "y"
        barrel3 = 90
        self.assertFalse(card.evaluate_response(barrel3, answer3, list7))
        list10 = [1, 32, 11, 45, 56]
        answer4 = "n"
        barrel4 = 90
        self.assertTrue(card.evaluate_response(barrel4, answer4, list10))

    def test_removesymbols(self):
        card = lotterycard("Player")
        list = [":",12,"#","fd","@",90]
        symbols = [":","#","@"]
        self.assertEqual(card.remove_symbols(list,symbols),str(["",12,"","fd","",90]))