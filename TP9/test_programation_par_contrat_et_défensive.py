from unittest import TestCase
from programation_par_contrat_et_défensive import Fraction


class TestFraction(TestCase):
    def test___init__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(-10, 5)
        frac3 = Fraction(10, -5)
        frac4 = Fraction(-10, -5)
        frac5 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.numerator, 0, "__init__ : test du numérateur par défaut")
        self.assertEqual(frac.denominator, 1, "__init__ : test du denominator par défaut")
        # 2 normal
        self.assertEqual(frac1.numerator, 10, "__init__ : test du numérateur normal")
        self.assertEqual(frac1.denominator, 5, "__init__ : test du denominator normal")
        # 3 négatif num
        self.assertEqual(frac2.numerator, -10, "__init__ : test du numérateur avec un num  négatif")
        self.assertEqual(frac2.denominator, 5, "__init__ : test du denominator négatif avec un num  négatif")
        # 4 négatif den
        self.assertEqual(frac3.numerator, -10, "__init__ : test du numérateur avec un den  négatif")
        self.assertEqual(frac3.denominator, 5, "__init__ : test du denominator normal avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac4.numerator, 10, "__init__ : test du numérateur normal avec un den et num  négatif")
        self.assertEqual(frac4.denominator, 5, "__init__ : test du denominator normal avec un den et num négatif")
        # 6 zéro num
        self.assertEqual(frac5.numerator, 0, "__init__ : test du numérateur avec un num égal à 0")
        self.assertEqual(frac5.denominator, 5, "__init__ : test du denominator avec un num égal à 0")
        # 7 raise: zéro den
        self.assertRaises(ZeroDivisionError, Fraction, 1, 0)
        pass

    def test___str__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(-10, 5)
        frac3 = Fraction(10, -5)
        frac4 = Fraction(-10, -5)
        frac5 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.__str__(), "0.0/1.0", "__str__ : test du numérateur par défaut")
        # 2 normal
        self.assertEqual(frac1.__str__(), "2.0/1.0", "__str__ : test du numérateur normal")
        # 3 négatif num
        self.assertEqual(frac2.__str__(), "-2.0/1.0", "__str__ : test du numérateur avec un num  négatif")
        # 4 négatif den
        self.assertEqual(frac3.__str__(), "-2.0/1.0", "__str__ : test du numérateur avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac4.__str__(), "2.0/1.0", "__str__ : test du numérateur normal avec un den et num  négatif")
        # 6 zéro num
        self.assertEqual(frac5.__str__(), "0.0/1.0", "__str__ : test du numérateur avec un num égal à 0")

    def test_as_mixed_number(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(-10, 5)
        frac3 = Fraction(10, -5)
        frac4 = Fraction(-10, -5)
        frac5 = Fraction(0, 5)
        frac6 = Fraction(11, 5)

        # 1 default
        self.assertEqual(frac.as_mixed_number(), "0 + 0.0/1.0", "as_mixed_number : test par défaut")
        # 2.1 normal
        self.assertEqual(frac1.as_mixed_number(), "2 + 0.0/1.0", "as_mixed_number : test  normal 1")
        # 2.2 normal 1
        self.assertEqual(frac6.as_mixed_number(), "2 + 1.0/5.0", "as_mixed_number : test normal 2")
        # 3 négatif num
        self.assertEqual(frac2.as_mixed_number(), "-2 + 0.0/1.0", "as_mixed_number : test avec un num  négatif")
        # 4 négatif den
        self.assertEqual(frac3.as_mixed_number(), "-2 + 0.0/1.0", "as_mixed_number : test avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac4.as_mixed_number(), "2 + 0.0/1.0",
                         "as_mixed_number : test normal avec un den et num  négatif")
        # 6 zéro num
        self.assertEqual(frac5.as_mixed_number(), "0 + 0.0/1.0", "as_mixed_number : test avec un num égal à 0")

    def test___add__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        frac4 = Fraction(10, -5)
        frac5 = Fraction(-10, -5)
        frac6 = Fraction(0, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        other3 = Fraction(-10, 5)
        other4 = Fraction(10, -5)
        other5 = Fraction(-10, -5)
        other6 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.__add__(other).__str__(), "0.0/1.0", "__add__ : test du str par défaut")
        # 2 normal
        self.assertEqual(frac1.__add__(other2).__str__(), "21.0/5.0", "__add__ : test du str normal 1")
        # 3 négatif num
        self.assertEqual(frac3.__add__(other1).__str__(), "0.0/1.0", "__add__ : test du str avec un num negatif ")
        # 4 négatif den
        self.assertEqual(frac4.__add__(other2).__str__(), "1.0/5.0", "__add__ : test du str avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac2.__add__(other5).__str__(), "21.0/5.0",
                         "__add__ : test du str avec un nagatif num and den")
        # 6 nagatif num and den
        self.assertEqual(frac3.__add__(other5).__str__(), "0.0/1.0",
                         "__add__ : test du str avec un nagatif num and den")
        # 7 nagatif num and den
        self.assertEqual(frac6.__add__(other1).__str__(), "2.0/1.0", "__add__ : test du str normal avec num = 0")
        # 8 zéro num
        self.assertEqual(frac6.__add__(other3).__str__(), "-2.0/1.0",
                         "__add__ : test du str avec un zéro num + negatif num")
        # 9 zéro num
        self.assertEqual(frac6.__add__(other4).__str__(), "-2.0/1.0",
                         "__add__ : test du str avec un zéro num + negatif num")

    def test___sub__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        frac4 = Fraction(10, -5)
        frac5 = Fraction(-10, -5)
        frac6 = Fraction(0, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        other3 = Fraction(-10, 5)
        other4 = Fraction(10, -5)
        other5 = Fraction(-10, -5)
        other6 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.__sub__(other).__str__(), "0.0/1.0", "__sub__ : test du str par défaut")
        # 2 normal
        self.assertEqual(frac1.__sub__(other2).__str__(), "-1.0/5.0", "__sub__ : test du str normal 1")
        # 3 négatif num
        self.assertEqual(frac3.__sub__(other1).__str__(), "-4.0/1.0", "__sub__ : test du str avec un num negatif ")
        # 4 négatif den
        self.assertEqual(frac4.__sub__(other2).__str__(), "-21.0/5.0", "__sub__ : test du str avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac2.__sub__(other5).__str__(), "1.0/5.0",
                         "__sub__ : test du str avec un nagatif num and den")
        # 6 nagatif num and den
        self.assertEqual(frac3.__sub__(other5).__str__(), "-4.0/1.0",
                         "__sub__ : test du str avec un nagatif num and den")
        # 7 nagatif num and den
        self.assertEqual(frac6.__sub__(other1).__str__(), "-2.0/1.0", "__sub__ : test du str normal avec num = 0")
        # 8 zéro num
        self.assertEqual(frac6.__sub__(other3).__str__(), "2.0/1.0",
                         "__sub__ : test du str avec un zéro num + negatif num")
        # 9 zéro num
        self.assertEqual(frac6.__sub__(other4).__str__(), "2.0/1.0",
                         "__sub__ : test du str avec un zéro num + negatif num")

    def test___eq__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        frac4 = Fraction(10, -5)
        frac5 = Fraction(-10, -5)
        frac6 = Fraction(0, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        other3 = Fraction(-10, 5)
        other4 = Fraction(10, -5)
        other5 = Fraction(-10, -5)
        other6 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.__eq__(other), True, "__add__ : test par défaut")
        # 2 normal
        self.assertEqual(frac1.__eq__(other2), False, "__add__ : test normal")
        # 3 négatif num
        self.assertEqual(frac3.__eq__(other1), False, "__add__ : test avec un num et den negatif ")
        # 4 négatif den
        self.assertEqual(frac4.__eq__(other4), True, "__add__ : test avec un den négatif")
        # 5 nagatif num and den
        self.assertEqual(frac1.__eq__(other5), True, "__add__ : test avec un nagatif num and den")
        # 6 nagatif num and den
        self.assertEqual(frac3.__eq__(other5), False, "__add__ : test avec un nagatif num and den")
        # 7 nagatif num and den
        self.assertEqual(frac6.__eq__(other1), False, "__add__ : test normal avec num = 0")
        # 8 zéro num
        self.assertEqual(frac6.__eq__(other3), False, "__add__ : test avec un zéro num + negatif num")
        # 9 zéro num
        self.assertEqual(frac6.__eq__(other6), True, "__add__ : test avec deux zéro num ")

    def test_is_integer(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(0, 5)
        frac4 = Fraction(0, -5)
        frac5 = Fraction(4, 5)
        frac6 = Fraction(5, 5)

        # 1 default
        self.assertEqual(frac.is_integer(), True, "is_integer : où self à ses parametres par défaut")
        # 2 normal
        self.assertEqual(frac2.is_integer(), False, "is_integer : où tout est normal")
        # 3 integer
        self.assertEqual(frac1.is_integer(), True, "is_integer :ou self est un integer")
        # 4 zero
        self.assertEqual(frac3.is_integer(), True, "is_integer : ou self est égal à 0")
        # 5 negative zero
        self.assertEqual(frac4.is_integer(), True, "is_integer : ou self est égal à un zéro negatif")
        # 6 proper
        self.assertEqual(frac5.is_integer(), False, "is_integer : ou self est proper")
        # 7 unit
        self.assertEqual(frac6.is_integer(), True, "is_integer : ou self est un unit")

    def test_is_proper(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(0, 5)
        frac4 = Fraction(0, -5)
        frac5 = Fraction(4, 5)
        frac6 = Fraction(5, 5)

        # 1 default
        self.assertEqual(frac.is_proper(), True, "is_proper : où self à ses parametres par défaut")
        # 2 normal
        self.assertEqual(frac2.is_proper(), False, "is_proper : où tout est normal")
        # 3 integer
        self.assertEqual(frac1.is_proper(), False, "is_proper :ou self est un integer")
        # 4 zero
        self.assertEqual(frac3.is_proper(), True, "is_proper : ou self est égal à 0")
        # 5 negative zero
        self.assertEqual(frac4.is_proper(), True, "is_proper : ou self est égal à un zéro negatif")
        # 6 proper
        self.assertEqual(frac5.is_proper(), True, "is_proper : ou self est proper")
        # 7 unit

    def test_is_adjacent_to(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(-10, 5)
        frac3 = Fraction(5, 5)
        frac4 = Fraction(-10, -5)
        frac5 = Fraction(-5, 5)
        frac6 = Fraction(11, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(-10, 5)
        other3 = Fraction(10, -5)
        other4 = Fraction(-10, -5)
        other5 = Fraction(0, 5)
        other6 = Fraction(5, 5)

        # 1 default
        self.assertEqual(frac.is_adjacent_to(other), False, "is_adjacent_to : test par défaut")
        # 2 normal
        self.assertEqual(frac6.is_adjacent_to(other1), False, "is_adjacent_to : test  normal 1")
        # 3 equal
        self.assertEqual(frac1.is_adjacent_to(other1), False, "is_adjacent_to : ou other et self sont identique ")
        # 4 adjacent +1
        self.assertEqual(frac3.is_adjacent_to(other1), True, "is_adjacent_to : ou il sont adjacent +1")
        # 5 adjacent -1
        self.assertEqual(frac3.is_adjacent_to(other5), True, "is_adjacent_to : ou il sont adjacent -1")
        # 6 adjacent -1 negatif
        self.assertEqual(frac5.is_adjacent_to(other2), True, "is_adjacent_to : ou il sont adjacent -1 en négatif")
        # 7 adjacent -1 negatif et zero
        self.assertEqual(frac5.is_adjacent_to(other5), True,"is_adjacent_to : ou il sont adjacent +1 en négatif et zéro")
        # 8 adjacent  full negatif and positif
        self.assertEqual(frac4.is_adjacent_to(other6), True,"is_adjacent_to : ou il sont adjacent full négatif et posifir")


