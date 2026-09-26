# Fraction — Custom Python Data Type

A custom **Fraction class in Python** built using Object-Oriented Programming (OOP).

This project implements fractions from scratch and provides arithmetic operations, comparisons, conversions, and utility methods without relying on Python's built-in `fractions.Fraction` class.

## Features

The `Fraction` class supports:

* Fraction creation using numerator and denominator
* String representation
* Addition and subtraction
* Multiplication and division
* Floor division
* Modulo operation
* Comparison operators
* Unary negation
* Absolute value
* Reverse arithmetic operations
* Integer and float conversion
* Reciprocal calculation
* Integer powers
* Decimal-to-fraction conversion
* String-to-fraction conversion
* Mixed fraction conversion
* Proper/improper fraction checking
* Whole-number checking
* Decimal conversion
* Percentage conversion
* Fraction simplification using GCD

## OOP Concepts Used

This project demonstrates several important Python OOP concepts:

### 1. Class and Objects

The `Fraction` class represents a fraction using two attributes:

```python
num
denom
```

Example:

```python
f = Fraction(3, 4)
```

Here, `f` is an object of the `Fraction` class.

### 2. Constructor

The `__init__()` method initializes the numerator and denominator.

```python
def __init__(self, n, d):
    self.num = n
    self.denom = d
```

It also validates the denominator to prevent division by zero.

### 3. Dunder / Magic Methods

The project makes extensive use of Python's special methods.

Examples:

```python
__add__()
__sub__()
__mul__()
__truediv__()
__eq__()
__lt__()
__gt__()
__neg__()
__abs__()
__float__()
__int__()
__pow__()
```

This allows objects of the `Fraction` class to behave similarly to normal numbers.

For example:

```python
f1 + f2
f1 * f2
f1 == f2
float(f1)
```

### 4. Operator Overloading

Arithmetic operators are overloaded to work with fraction objects.

For example:

```python
f1 + f2
f1 - f2
f1 * f2
f1 / f2
```

The class also supports operations between fractions and integers.

Example:

```python
Fraction(3, 4) + 2
```

### 5. Reverse Operator Overloading

Reverse magic methods allow expressions where the integer appears first.

Examples:

```python
2 + Fraction(3, 4)
2 - Fraction(3, 4)
2 * Fraction(3, 4)
2 / Fraction(3, 4)
```

Implemented methods include:

```python
__radd__()
__rsub__()
__rmul__()
__rfloordiv__()
__rtruediv__()
__rmod__()
```

### 6. Class Method

`from_decimal()` provides an alternative way of creating a fraction from a decimal value.

Example:

```python
Fraction.from_decimal(0.75)
```

The decimal is converted into a fraction and simplified.

### 7. Encapsulation Through Methods

Fraction-related operations are kept inside the `Fraction` class instead of being implemented separately throughout the program.

Examples:

```python
f.simplify()
f.to_decimal()
f.to_percentage()
f.to_mixed()
```

## Supported Operations

### Arithmetic

The class provides:

| Operation      | Method           |
| -------------- | ---------------- |
| Addition       | `__add__()`      |
| Subtraction    | `__sub__()`      |
| Multiplication | `__mul__()`      |
| Division       | `__truediv__()`  |
| Floor Division | `__floordiv__()` |
| Modulo         | `__mod__()`      |
| Power          | `__pow__()`      |
| Negation       | `__neg__()`      |
| Absolute Value | `__abs__()`      |

### Comparisons

The following comparison operators are supported:

```python
==
!=
>
>=
<
<=
```

Implemented using:

```python
__eq__()
__ne__()
__gt__()
__ge__()
__lt__()
__le__()
```

### Type Conversion

The class supports:

```python
float(fraction)
int(fraction)
```

through:

```python
__float__()
__int__()
```

## Fraction Utilities

### Simplification

Fractions are simplified using Python's `math.gcd()`.

```python
f.simplify()
```

For example:

```text
8/12 → 2/3
```

### Reciprocal

The reciprocal of a fraction can be obtained using:

```python
f.__reciprocal__()
```

For example:

```text
3/5 → 5/3
```

### Decimal Conversion

```python
f.to_decimal()
```

Converts the fraction into a decimal value.

### Percentage Conversion

```python
f.to_percentage()
```

Converts the fraction into percentage form.

Example:

```text
3/4 → 75%
```

### Mixed Fraction

```python
f.to_mixed()
```

Converts an improper fraction into a mixed fraction.

Example:

```text
7/3 → 2 1/3
```

### Fraction Classification

The class provides methods to determine whether a fraction is:

```python
f.is_proper()
f.is_improper()
f.is_whole()
```

### Decimal to Fraction

A decimal can be converted into a fraction using:

```python
Fraction.from_decimal(0.625)
```

Conceptually:

```text
0.625 → 625/1000 → 5/8
```

### String to Fraction

A fraction can also be created from a string representation such as:

```text
"3/4"
```

using the `from_string()` method.

## Example Usage

```python
from fraction import Fraction

f1 = Fraction(3, 4)
f2 = Fraction(2, 5)

print(f1)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)

print(f1 == f2)
print(float(f1))
print(int(f1))

print(f1.to_decimal())
print(f1.to_percentage())
```

## Project Structure

```text
Fraction/
│
├── fraction.py
└── README.md
```

`fraction.py` contains the complete implementation of the custom `Fraction` class.

`README.md` contains the project documentation.

## Technologies Used

* Python
* Object-Oriented Programming
* `math` module
* Magic/Dunder Methods
* Operator Overloading

## Learning Outcomes

This project helped implement and understand:

* Python classes and objects
* Constructors
* Instance methods
* Class methods
* Operator overloading
* Magic methods
* Reverse operators
* Type conversion
* Exception handling
* GCD-based simplification
* String parsing
* Basic numerical algorithms

## Future Improvements

Possible improvements for future versions include:

* Automatic simplification during object creation
* Better support for negative denominators
* Support for decimal values with repeating patterns
* Improved modulo implementation
* More robust input validation
* Support for multiplication/division with floating-point values
* Proper `__repr__()` implementation
* Hashing support using `__hash__()`
* Unit testing using Python's `unittest` or `pytest`
* Packaging the class as an installable Python library

## Note

This project is implemented from scratch for learning and demonstrates how Python's OOP features can be used to create a custom numerical data type.

It is intended as an educational implementation rather than a replacement for Python's production-ready `fractions.Fraction` module.
