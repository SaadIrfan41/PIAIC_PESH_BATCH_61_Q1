a: int = 5
b: int = 5

print(a + b)  # addtition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a // b)  # floor division (quotient)
print(-(-a // b))  # Ceil division (quotient)
print(a % b)  # modulus (remainder)
print(a**b)  # exponentiation (power)

"""
Assignment Operators
+=
-=
*=
/=
//=
%=
**=
"""
c = 5
print(c)
c += 2  # equivalent to c = c + 2
print(c)
c = 5
c -= 2  # equivalent to c = c - 2
print(c)
c = 5
c *= 2  # equivalent to c = c * 2
print(c)
c = 5
c /= 2  # equivalent to c = c / 2
print(c)
c = 5
c //= 2  # equivalent to c = c // 2
print(c)
c = 5
c %= 2  # equivalent to c = c % 2
print(c)
c = 5
c **= 2  # equivalent to c = c ** 2
print(c)

# ? Comparison Operators
"""
== Equal to
!= Not equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

"""
d = int(input("Enter the value for d: "))
e = int(input("Enter the value for e: "))
print("Are They Equal? ", d == e)  # Equal to
print("Are They Not Equal? ", d != e)  # Not equal to
print("Is d Greater than e?", d > e)  # Greater than
print("Is d Less than e? ", d < e)  # Less than
print("Is d Greater than or Equal to e", d >= e)  # Greater than or equal to
print("Is d Less than or Equal to e", d <= e)  # Less than or equal to
"""
Logical Operators
and
or
not
"""
f = int(input("Enter the value for f: "))
g = int(input("Enter the value for g: "))
print(
    "Is f Less than g and f is Equal to g", f < g and f == g
)  # False (both conditions must be true)
print(
    "Is f Less than g or f is Equal to g", f < g or f == g
)  # True (at least one condition must be true)
print(
    "Is f Less than g and f is Equal to g return the Opposite of that",
    not (f < g and f == g),
)  # True (opposite of the previous condition)
"""
Identity Operators
is
is not
"""
h = 5
i = 6
j = 5
print(h is i)  # False (h and i are not the same)
print(h is j)  # True (h and j are the same)
print(h is not i)  # True (h and i are not the same)

n = 5
o = 6
p = 7
q = 8

# * and / have higher precedence than + and -
print(n + o * p)  # 47 (5 + 6 * 7)
print(n + o * p / q)  # 10.25 (5 + 6 * 7 / 8)
print((n + o) * p / q)  # 9.625 (5 + 6) * 7 / 8)
