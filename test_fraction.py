import unittest
from my_fraction import Fraction

class TestFraction(unittest.TestCase):
    # Constructor and String
    def test_creation(self):
        f = Fraction(3, 4)

        self.assertEqual(f.num, 3)
        self.assertEqual(f.denom, 4)

    def test_string(self):
        f = Fraction(3, 4)

        self.assertEqual(str(f), "3/4")

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            Fraction(3, 0)

    def test_negative_denominator(self):
        f = Fraction(3, -4)

        self.assertEqual(f.num, -3)
        self.assertEqual(f.denom, 4)


    # -------------------------
    # Simplification
    # -------------------------

    def test_simplify(self):
        f = Fraction(8, 12)

        self.assertEqual(f.num, 2)
        self.assertEqual(f.denom, 3)


    # -------------------------
    # Addition
    # -------------------------

    def test_addition(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)

        result = f1 + f2

        self.assertEqual(result, Fraction(5, 6))

    def test_add_integer(self):
        f = Fraction(1, 2)

        result = f + 2

        self.assertEqual(result, Fraction(5, 2))

    def test_reverse_addition(self):
        f = Fraction(1, 2)

        result = 2 + f

        self.assertEqual(result, Fraction(5, 2))


    # -------------------------
    # Subtraction
    # -------------------------

    def test_subtraction(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 4)

        result = f1 - f2

        self.assertEqual(result, Fraction(1, 2))

    def test_reverse_subtraction(self):
        f = Fraction(1, 2)

        result = 2 - f

        self.assertEqual(result, Fraction(3, 2))


    # -------------------------
    # Multiplication
    # -------------------------

    def test_multiplication(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)

        result = f1 * f2

        self.assertEqual(result, Fraction(1, 2))

    def test_reverse_multiplication(self):
        f = Fraction(3, 4)

        result = 2 * f

        self.assertEqual(result, Fraction(3, 2))


    # -------------------------
    # Division
    # -------------------------

    def test_division(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 3)

        result = f1 / f2

        self.assertEqual(result, Fraction(9, 8))

    def test_division_by_zero(self):
        f = Fraction(3, 4)

        with self.assertRaises(ZeroDivisionError):
            f / Fraction(0, 1)

    def test_reverse_division(self):
        f = Fraction(2, 3)

        result = 2 / f

        self.assertEqual(result, Fraction(3, 1))


    # Floor Division


    def test_floor_division(self):
        f1 = Fraction(7, 3)
        f2 = Fraction(2, 3)

        result = f1 // f2

        self.assertEqual(result, 3)

    def test_reverse_floor_division(self):
        f = Fraction(2, 3)

        result = 2 // f

        self.assertEqual(result, 3)



    # Modulo


    def test_modulo(self):
        f1 = Fraction(7, 3)
        f2 = Fraction(2, 3)

        result = f1 % f2

        self.assertEqual(result, Fraction(1, 3))

    def test_reverse_modulo(self):
        f = Fraction(2, 3)

        result = 2 % f

        self.assertEqual(result, Fraction(0, 1))


    # Comparisons


    def test_equal(self):
        self.assertEqual(Fraction(1, 2), Fraction(2, 4))

    def test_not_equal(self):
        self.assertNotEqual(Fraction(1, 2), Fraction(3, 4))

    def test_greater_than(self):
        self.assertTrue(Fraction(3, 4) > Fraction(1, 2))

    def test_greater_than_or_equal(self):
        self.assertTrue(Fraction(3, 4) >= Fraction(3, 4))

    def test_less_than(self):
        self.assertTrue(Fraction(1, 4) < Fraction(1, 2))

    def test_less_than_or_equal(self):
        self.assertTrue(Fraction(1, 2) <= Fraction(1, 2))


    # Unary Operations


    def test_negative(self):
        f = Fraction(3, 4)

        result = -f

        self.assertEqual(result, Fraction(-3, 4))

    def test_absolute(self):
        f = Fraction(-3, 4)

        result = abs(f)

        self.assertEqual(result, Fraction(3, 4))



    # Type Conversion

    def test_float_conversion(self):
        f = Fraction(1, 2)

        self.assertEqual(float(f), 0.5)

    def test_integer_conversion(self):
        f = Fraction(7, 3)

        self.assertEqual(int(f), 2)


    # Reciprocal


    def test_reciprocal(self):
        f = Fraction(3, 4)

        result = f.reciprocal()

        self.assertEqual(result, Fraction(4, 3))

    def test_reciprocal_of_zero(self):
        f = Fraction(0, 1)

        with self.assertRaises(ZeroDivisionError):
            f.reciprocal()


    # Power

    def test_power(self):
        f = Fraction(2, 3)

        result = f ** 2

        self.assertEqual(result, Fraction(4, 9))

    def test_power_zero(self):
        f = Fraction(5, 7)

        result = f ** 0

        self.assertEqual(result, Fraction(1, 1))



    # Fraction Classification


    def test_proper_fraction(self):
        f = Fraction(2, 5)

        self.assertTrue(f.is_proper())

    def test_improper_fraction(self):
        f = Fraction(7, 5)

        self.assertTrue(f.is_improper())

    def test_whole_fraction(self):
        f = Fraction(8, 4)

        self.assertTrue(f.is_whole())


    # -------------------------
    # Mixed Fraction
    # -------------------------

    def test_mixed_fraction(self):
        f = Fraction(7, 3)

        self.assertEqual(f.to_mixed(), "2 1/3")

    def test_mixed_whole_number(self):
        f = Fraction(6, 3)

        self.assertEqual(f.to_mixed(), "2")


    # -------------------------
    # Decimal Conversion
    # -------------------------

    def test_decimal(self):
        f = Fraction(1, 4)

        self.assertEqual(f.to_decimal(), 0.25)

    def test_decimal_to_fraction(self):
        f = Fraction.from_decimal(0.75)

        self.assertEqual(f, Fraction(3, 4))

    def test_decimal_to_fraction_negative(self):
        f = Fraction.from_decimal(-0.5)

        self.assertEqual(f, Fraction(-1, 2))


    # -------------------------
    # Percentage
    # -------------------------

    def test_percentage(self):
        f = Fraction(3, 4)

        self.assertEqual(f.to_percentage(), "75.0%")


    # -------------------------
    # String Conversion
    # -------------------------

    def test_from_string(self):
        f = Fraction.from_string("6/8")

        self.assertEqual(f, Fraction(3, 4))

    def test_from_string_with_spaces(self):
        f = Fraction.from_string(" 6 / 8 ")

        self.assertEqual(f, Fraction(3, 4))

    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            Fraction.from_string("6")


    if __name__ == "__main__":
        unittest.main()
obj1=TestFraction()


