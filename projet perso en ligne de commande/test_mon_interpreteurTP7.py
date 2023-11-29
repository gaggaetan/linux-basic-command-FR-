from unittest import TestCase
from mon_interpreteurTP7 import mon_interpreteurTP7
from programation_par_contrat import Fraction


class Test_mon_interpreteurTP7(TestCase):

    def test_make_fraction(self):
        interpreteurObject = mon_interpreteurTP7()
        frac1 = interpreteurObject.makeFraction(10, 5)
        frac2 = interpreteurObject.makeFraction(10, -5)

        # normal
        self.assertEqual(frac1.__str__(), Fraction(10, 5).__str__(), "test")
        #negatif
        self.assertEqual(frac2.__str__(), Fraction(10, -5).__str__(), "test")
        #den égal 0
        self.assertRaises(ZeroDivisionError,interpreteurObject.makeFraction, 10, 0)


    def test_fractions_management(self):
        interpreteurObject = mon_interpreteurTP7()
        frac1 = interpreteurObject.fractionsManagement("10 5")
        frac2 = interpreteurObject.fractionsManagement("10 -5")

        # normal
        self.assertEqual(frac1.__str__(), Fraction(10, 5).__str__(), "test")
        # negatif
        self.assertEqual(frac2.__str__(), Fraction(10, -5).__str__(), "test")
        # den égal "10 string"
        self.assertRaises(ValueError, interpreteurObject.fractionsManagement, "10 string")

    def test_do_find_integer_fractions(self):
        interpreteurObject = mon_interpreteurTP7()

        # normal
        self.assertEqual(interpreteurObject.do_find_integer_fractions("1 2 6 6 5 1"), "1.0/1.0\n5.0/1.0",
                         "mon_interpreteurTP7 : test avec en parametres 1 2 6 6 5 1")
        # négative
        self.assertEqual(interpreteurObject.do_find_integer_fractions("1 2 -6 6 5 -1"), "-1.0/1.0\n-5.0/1.0",
                         "mon_interpreteurTP7 : test avec en parametres 1 2 -6 6 5 -1")
        # not pair param
        self.assertRaises(ValueError, interpreteurObject.do_find_integer_fractions, "1 2 6")
        # no parram
        self.assertRaises(ValueError, interpreteurObject.do_find_integer_fractions, "")
