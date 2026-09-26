import math


class Fraction:

    def __init__(self, n, d):
        if d == 0:
            raise ValueError("denominator cannot be zero")

        if d < 0:
            n = -n
            d = -d

        self.num = n
        self.denom = d
        self.simplify()

    def __str__(self):
        return "{}/{}".format(self.num, self.denom)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        temp_num = self.num * other.denom + self.denom * other.num
        temp_denom = self.denom * other.denom

        return Fraction(temp_num, temp_denom)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        temp_num = self.num * other.denom - self.denom * other.num
        temp_denom = self.denom * other.denom

        return Fraction(temp_num, temp_denom)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        temp_num = self.num * other.num
        temp_denom = self.denom * other.denom

        return Fraction(temp_num, temp_denom)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        if other.num == 0:
            raise ZeroDivisionError("cannot divide by zero")

        temp_num = self.num * other.denom
        temp_denom = self.denom * other.num

        return Fraction(temp_num, temp_denom)

    def __floordiv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        if other.num == 0:
            raise ZeroDivisionError("cannot divide by zero")

        return (self.num * other.denom) // (self.denom * other.num)

    def __mod__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        if other.num == 0:
            raise ZeroDivisionError("cannot divide by zero")

        quotient = (self / other)
        floor_value = math.floor(float(quotient))

        return self - (Fraction(floor_value, 1) * other)

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        return self.num * other.denom == self.denom * other.num

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        return self.num * other.denom > self.denom * other.num

    def __ge__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        return self.num * other.denom >= self.denom * other.num

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        return self.num * other.denom < self.denom * other.num

    def __le__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        return self.num * other.denom <= self.denom * other.num

    def __neg__(self):
        return Fraction(-self.num, self.denom)

    def __abs__(self):
        return Fraction(abs(self.num), self.denom)

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return Fraction(other, 1) - self

    def __rmul__(self, other):
        return self * other

    def __rfloordiv__(self, other):
        return Fraction(other, 1) // self

    def __rtruediv__(self, other):
        return Fraction(other, 1) / self

    def __rmod__(self, other):
        return Fraction(other, 1) % self

    def __float__(self):
        return self.num / self.denom

    def __int__(self):
        return self.num // self.denom

    def reciprocal(self):
        if self.num == 0:
            raise ZeroDivisionError("cannot take reciprocal of zero")

        return Fraction(self.denom, self.num)

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError("power must be an integer")

        return Fraction(self.num ** power, self.denom ** power)

    def simplify(self):
        gcd = math.gcd(self.num, self.denom)

        self.num //= gcd
        self.denom //= gcd

        return self

    def to_mixed(self):
        if abs(self.num) < self.denom:
            return str(self)

        whole = self.num // self.denom
        remainder = abs(self.num) % self.denom

        if remainder == 0:
            return str(whole)

        return "{} {}/{}".format(whole, remainder, self.denom)

    def is_improper(self):
        return abs(self.num) >= self.denom

    def is_proper(self):
        return abs(self.num) < self.denom

    def is_whole(self):
        return self.num % self.denom == 0

    def to_decimal(self):
        return self.num / self.denom

    def to_percentage(self):
        return "{}%".format((self.num / self.denom) * 100)

    @classmethod
    def from_decimal(cls, value):
        value = str(value).strip()

        if "." not in value:
            return cls(int(value), 1)

        negative = value.startswith("-")

        if negative:
            value = value[1:]

        whole, decimal = value.split(".")

        denom = 10 ** len(decimal)
        num = int(whole) * denom + int(decimal)

        if negative:
            num = -num

        return cls(num, denom)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            raise TypeError("value must be a string")

        parts = value.strip().split("/")

        if len(parts) != 2:
            raise ValueError('invalid fraction format. Use "a/b"')

        numerator = int(parts[0].strip())
        denominator = int(parts[1].strip())

        return cls(numerator, denominator)