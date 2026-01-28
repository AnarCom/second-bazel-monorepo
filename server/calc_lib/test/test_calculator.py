from server.calc_lib.src.Calculator import Calculator
# import unittest

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    print("a")

# class TestCalculator(unittest.TestCase):
#     def setUp(self):
#         self.calc = Calculator()

#     def test_add(self):
#         self.assertEqual(self.calc.add(2, 3), 5)
#         self.assertEqual(self.calc.add(-1, 1), 0)
#         print("a")

#     def test_subtract(self):
#         self.assertEqual(self.calc.subtract(5, 3), 2)
#         self.assertEqual(self.calc.subtract(0, 0), 0)
#         print("b")

#     def test_multiply(self):
#         self.assertEqual(self.calc.multiply(4, 3), 12)
#         self.assertEqual(self.calc.multiply(-1, 5), -5)
#         print("c")

#     def test_divide(self):
#         self.assertEqual(self.calc.divide(10, 2), 5)
#         self.assertEqual(self.calc.divide(-6, 3), -2)
#         with self.assertRaises(ValueError):
#             self.calc.divide(5, 0)
#         print("d")