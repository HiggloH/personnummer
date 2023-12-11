import random
import os

skott = False

antal_number = 10
max_dagar = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

alla = []


# Generera en månad
def gen_m():
    max_number = 12
    min_number = 1

    m = random.randint(min_number, max_number)

    if skott and m == 2:
        max_dagar[2] += 1

    return m


# Generera en dag utifrån vilken månad den genererade
def gen_d(m):
    max_number = max_dagar[m]
    min_number = 1

    d = random.randint(min_number, max_number)

    return d


# Generera ett årtal
def gen_y():
    global skott

    max_number = 2025
    min_number = 1899

    y = random.randint(min_number, max_number)

    if y <= 1925:
        tecken = "+"
    else:
        tecken = "-"

    # kolla ifall det är ett skott år
    skott = (int(y) % 4) == 0
    if int(y) % 100 == 0:
        if int(y) % 400 == 0:
            skott = True
        else:
            skott = False

    y = list(str(y))

    # Gör om det till formatet åå istället för åååå
    del y[0]
    del y[0]

    yy = ""

    for n in y:
        yy += n

    return yy, tecken


# Generera de fyra sista siffrorna
def gen_last():
    max_num = 9

    # Generera fyra siffror mellan 0 och 9
    number_1 = str(random.randint(0, max_num))
    number_2 = str(random.randint(0, max_num))
    number_3 = str(random.randint(0, max_num))
    number_4 = str(random.randint(0, max_num))

    # Sätt ihop siffrorna till ett tal
    hole_number = number_1 + number_2 + number_3 + number_4

    return hole_number


# Kombinera år, månad, dag, tecken och de fyra sista till ett personnummer
def combine(y, m, d, tecken, last):
    if m < 10:
        m = "0" + str(m)
    else:
        m = str(m)

    if d < 10:
        d = "0" + str(d)
    else:
        d = str(d)

    hole = str(y) + str(m) + str(d) + tecken + str(last) + "\n"

    # Lägg till personnumret till en lista med alla andra personnummer som den har genererat
    alla.append(hole)


def start():
    y = gen_y()
    tecken = y[1]
    y = y[0]

    m = gen_m()
    d = gen_d(m)

    last_four = gen_last()

    combine(y, m, d, tecken, last_four)


def change_antal(nytt_antal):
    global antal_number

    antal_number = nytt_antal


# Spara listan med alla personnummer till en text fil
def log():
    file = open("numbers.txt", "w")
    file.writelines(alla)
    file.close()


def start_gen():
    global max_dagar
    # Ta bort den gamla filen med gamla personnummer
    if os.path.exists("numbers.txt"):
        os.remove("numbers.txt")

    for n in range(0, antal_number):
        max_dagar = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        start()

    log()
