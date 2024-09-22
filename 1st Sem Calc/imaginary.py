import math


def checker_i(user):
    imaginary_number0 = ""
    oprtor = False
    cap: int = 0
    operators = ["+", "-"]
    neg = False

    for i in user:
        # condition for imaginary
        if i == "i":
            # sets it to an imaginary number
            position = user.index("i")  # checks index of that number
            positioning = position

            # loop that searches for an operator
            while oprtor is False:
                if user[positioning] in operators:  # if that value is in operator
                    oprtor = True
                    if user[positioning] == "-":
                        neg = True
                    cue = user[positioning]
                    cap = user.index(cue, 1)

                else:

                    positioning -= 1  # it'll stop at -1 when the next value is an operator

            if positioning == position - 1:  # for things like i43
                imaginary_number0 += user[position + 1:]

            else:  # for things like 43i

                imaginary_number0 += user[cap + 1:position]

                # z = 12 + i33

    num2 = int(imaginary_number0)
    if neg:
        num2 *= -1
    return num2


def checker_r(user):
    real_number0 = ""
    a = 0
    operators = ["+", "-"]

    for i in user:
        if i in operators:
            a: object = user.index(i)
            if user.count("-") > 1:
                a = user.index("-", 1)

    real_number0 += user[0:a]

    real_number0 = float(real_number0)
    return real_number0


def polar_checker_arg(user):
    arg = ""
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    a = user.index("s")+2
    for i in user[a:]:
        if i in numbers or i == "-" or i == "(":
            arg += i
        else:
            break
    arg = float(arg)
    return arg


def euler_checker_arg(user):
    arg = ""
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    a = user.index("i")+1
    for i in user[a:]:
        if i in numbers or i == "-" or i == "(":
            arg += i
        else:
            break
    arg = float(arg)
    return arg


def polar_checker_mod(user):
    mod = ""
    for i in user:
        if i == "[":
            mod += user[0:user.index(i)]

    mod = float(mod)
    return mod


def euler_checker_mod(user):
    mod = ""
    for i in user:
        if i == "e":
            mod += user[0:user.index(i)]

    mod = float(mod)
    return mod


def converter_polar(im, real):
    arg = math.atan(im / real)
    arg *= (180 / 3.14159)
    r = (im ** 2 + real ** 2) ** 0.5
    polar = f"{round(r, 3)}[cos({round(arg, 3)}) + isin({round(arg, 3)})]"
    return polar


def converter_euler(im, real):
    arg = math.atan(im / real) * (180 / 3.14159)
    r = (im ** 2 + real ** 2) ** 0.5
    euler = f"{round(r, 2)}e^i({round(arg, 2)})"
    return euler


def ima_product(eqn1, eqn2):
    a = checker_r(eqn1)
    b = checker_i(eqn1)
    c = checker_r(eqn2)
    d = checker_i(eqn2)

    product = f"Product: \n{a * c - (b * d)}  +  ({a * c + (a * d)})i"
    return product


def ima_quotient(eqn1, eqn2):
    a = checker_r(eqn1)
    b = checker_i(eqn1)
    c = checker_r(eqn2)
    d = checker_i(eqn2)

    imaquotient = f"{round((a * c + b * d) / ((c ** 2) + (d ** 2)), 3)}+{round((a * d + b * c) / ((c ** 2) + (d ** 2)), 3)}i"




    return imaquotient
