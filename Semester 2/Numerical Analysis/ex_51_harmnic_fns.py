import math as m

# Declare the constant functions d and epsilon
D = 4
EPS = 1/(10 ** (D + 1))


def harmonic1():
    """Function finds the least n satisfying the inequality 1/n < ε, say n0 and calculates value sn0 for series 1/k^2"""
    n = 1
    while 1/n >= EPS:
        n += 1
    return sum(1 / (k ** 2) for k in range(1, n + 1))


def harmonic2():
    """Function finds the least n satisfying the inequality 3/(n + 1)! < ε, say n0 and calculates value sn0 for series 1/k!"""
    n = 1
    sn0 = 0
    factorial = 2
    while 3/factorial >= EPS:
        n += 1
        factorial *= (n + 1)
    factorial = 1
    for k in range(0, n+1):
        if k > 0:
            factorial *= k
        sn0 += 1 / factorial
    return sn0


def harmonic3():
    """Function finds the least n satisfying the inequality 1/(n + 1)^3 < ε, say n0 and calculates value sn0 for series 1/k^3"""
    n = 1
    while 1 / (n + 1) ** 3 >= EPS:
        n += 1
    return sum(1 / k ** 3 for k in range(1, n + 1))

print("Value sn0 for n0 satisfying the inequality 1/n < ε. We say that value sn0 is an approximate value of S with accuracy ε.")
print(f"sn0 = {round(harmonic1(), D + 2)}")
print(f"π^2/6 = {round((m.pi**2)/6, D + 2)}")
print()

print("Value sn0 for n0 satisfying the inequality 3/(n + 1)! < ε. We say that value sn0 is an approximate value of S with accuracy ε.")
print(f"sn0 = {round(harmonic2(), D + 2)}")
print(f"e = {round(m.e, D + 2)}")
print()

print("Value sn0 for n0 satisfying the inequality 1/(n + 1)^3 < ε. We say that value sn0 is an approximate value of S with accuracy ε.")
print(f"sn0 = {round(harmonic3(), D + 2)}")
