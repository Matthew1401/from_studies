## a + bx + cx^2 = 0 ##

def solutions(coef):
    a = coef[0]
    b = coef[1]
    c = coef[2]
    if c != 0:
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant > 0:
            x1 = (-b - discriminant ** (1 / 2)) / 2 * c
            x2 = (-b + discriminant ** (1 / 2)) / 2 * c
            return x1, x2
        elif discriminant == 0:
            x0 = -b / 2 * c
            return x0, None
        else:
            return None, 0
    else:
        return None, None


def printing_results(coef, root1, root2):
    a = coef[0]
    b = coef[1]
    c = coef[2]
    if root1 is None and root2 is None:
        print(f"Equation {a} + ({b})x + ({c})x^2 is not quadratic")
    elif root1 is None and root2 == 0:
        print(f"Equation {a} + ({b})x + ({c})x^2 has no real roots")
    elif root2 is None:
        print(f"Equation {a} + ({b})x + ({c})x^2 has unique real root x0 = {root1}")
    else:
        print(f"Equation {a} + ({b})x + ({c})x^2 has two real roots x1 = {root1}, x2 = {root2}")


coeffitients_list = [[4, -5, 1], [9, -6, 1], [2, 3, 5], [3, -6, 0], [4, 5, 1], [-5, 7, 3]]
for coeff in coeffitients_list:
    solution1, solution2 = solutions(coeff)
    printing_results(coeff, solution1, solution2)
