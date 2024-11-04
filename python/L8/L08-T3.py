# L08-T3: Python module fraction
#
# Submitted by: Md Hamidur Rahman Khan
#

from fractions import Fraction

print("Give the first fraction.")
Numerator1 = int(input("Give numerator (top):\n"))
Denominator1 = int(input("Give denominator (bottom):\n"))

print("Give the second fraction.")
Numerator2 = int(input("Give numerator (top):\n"))
Denominator2 = int(input("Give denominator (bottom):\n"))

Expotent = int(input("Give an exponent:\n"))

Fraction1 = Fraction(Numerator1, Denominator1)
Fraction2 = Fraction(Numerator2, Denominator2)

Sum = Fraction1 + Fraction2
Subtract = Fraction1 - Fraction2
Multiply = Fraction1 * Fraction2
Divide = Fraction1 / Fraction2
Power = Fraction(Fraction1**Expotent)

print(f"Sum: {Fraction1} + {Fraction2} = {Sum}")
print(f"Subtract: {Fraction1} - {Fraction2} = {Subtract}")
print(f"Multiply: ({Fraction1}) * ({Fraction2}) = {Multiply}")
print(f"Divide: ({Fraction1}) / ({Fraction2}) = {Divide}")
print(f"Power: ({Fraction1})**{Expotent} = {Power}")