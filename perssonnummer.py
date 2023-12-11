running = True

n_number = ["19", "20"]
# Då är det 1900-talet
n_span = [25, 99]
m_nummer = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
# Max antal dager per månad, februari har två max antal beroende på om det är skottår
dagar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Två listor för felaktiga och korrekta personnummer
korrekta = []
felaktiga = []

# Listor för könen
killar = []
kvinnor = []

# För att logga födelseåren
years = {}


def algoritm(nummer, p: bool):
    nummer_list = list(nummer)

    # Kolla om personnumret är för kort
    if len(nummer_list) < 10:
        return print("Personnummer är för kort")
    elif len(nummer_list) > 10:
        return print("Person numret är för långt")
    else:
        # Gör om att element i personnumret till heltal
        for s in range(len(nummer_list)):
            nummer_list[s] = int(nummer_list[s])

        kolla_kon(nummer_list)

        sum_list = []

        # Gör Luhn-algoritmen för att kolla om personnumret är korrekt eller inte
        for n in range(len(nummer_list)):
            if n % 2 == 0:
                sum_list.append(nummer_list[n] * 2)
            else:
                sum_list.append(nummer_list[n] * 1)

            if sum_list[len(sum_list) - 1] >= 10:
                ny_list = list(str(sum_list[len(sum_list) - 1]))
                for s in range(len(ny_list)):
                    ny_list[s] = int(ny_list[s])
                nummer_sum = int(sum(ny_list))

                sum_list[len(sum_list) - 1] = nummer_sum

        summan = sum(sum_list)

        # Kolla om summan från luhn algoritm är delbar med tio, då är det ett korrekt personnummer
        if summan % 10 == 0:
            korrekta.append(nummer)
            if p:
                print("Det är ett korrekt personnummer")
            return
        else:
            felaktiga.append(nummer)
            if p:
                print("Det är inte ett korrekt personnummer")
            return


def kolla_kon(nummer):
    siffra = nummer[8]

    if siffra % 2 == 0:
        kvinnor.append(nummer)
    else:
        killar.append(nummer)


def kolla_inputen(pnr):
    # Kolla så att det inte finns några symboler som inte ska vara i personnumret
    try:
        for n in pnr:
            if n == "-":
                pass
            elif n == "+":
                pass
            else:
                n = int(n)
    except ValueError:
        return "c_error"

    utan = False

    gammal = False
    ung = False

    # Kolla så att personnumret är rätt längd
    if len(pnr) == 11:
        datum = pnr[:6]
    elif len(pnr) == 10:
        datum = pnr[:6]
        utan = True
    elif len(pnr) == 13:
        # Om pnr är 13 kan det vara ett ogiltigt personnummer eftersom det kan vara fler än fyra tal efter - eller + tecknet
        if "-" in pnr:
            t_index = pnr.index("-")
            d_length = pnr[:t_index]
            f_length = pnr[t_index:]

            # Kolla så att det är rätt mängd element före och efter tecknet
            if len(d_length) == 8:
                pass
            else:
                return "l_error"

            if len(f_length) == 5:
                pass
            else:
                return "l_error"

            ung = True
        elif "+" in pnr:
            t_index = pnr.index("+")
            d_length = pnr[:t_index]
            f_length = pnr[t_index:]

            # Kolla så att det är rätt mängd element före och efter tecknet
            if len(d_length) == 8:
                pass
            else:
                return "l_error"

            if len(f_length) == 5:
                pass
            else:
                return "l_error"

            gammal = True
        else:
            return "l_error"

        datum = pnr[:8]
    elif len(pnr) == 12:
        datum = pnr[:8]
        utan = True
    else:
        return "l_error"

    # Ta fram månaden året och dagen ur personnumret
    if len(datum) == 8:
        yy = datum[:4]
        mm = datum[4:6]
        dd = datum[6:]
    elif len(datum) == 6:
        yy = datum[:2]
        mm = datum[2:4]
        dd = datum[4:]

        if utan:
            if 25 < int(yy) < 99:
                yy = "19" + str(yy)
            else:
                yy = "20" + str(yy)
        elif not utan:
            tecken = pnr[6]

            if tecken == "-":
                if 25 < int(yy) < 99:
                    yy = "19" + str(yy)
                else:
                    yy = "20" + str(yy)
            elif tecken == "+":
                if 25 < int(yy) < 99:
                    yy = "18" + str(yy)
                else:
                    yy = "19" + str(yy)

    # Kolla  så att tecknet stämmer med året om året är skrivet åååå och det finns ett tecken
    if gammal:
        if int(yy) >= 1925:
            return "y_error"

    if ung:
        if int(yy) <= 1925:
            return "y_error"

    # kolla ifall det är ett skott år
    skott = (int(yy) % 4) == 0

    if int(yy) % 100 == 0:
        if int(yy) % 400 == 0:
            skott = True
        else:
            skott = False

    # Ändra antalet dagar i februari om det är skottår
    if skott:
        dagar[1] = 29
    else:
        dagar[1] = 28

    # Kolla så att månaden finns
    try:
        m_nummer.index(mm)
    except ValueError:
        return "m_error"

    # Kolla så att dagen är inom spanet av antal dagar i månaden
    if 1 <= int(dd) <= dagar[m_nummer.index(mm)]:
        pass
    else:
        return "d_error"

    rent_pnr = ""

    # Ta bort - eller + om det finns i personnumret
    if not utan:
        pnr = list(pnr)
        if pnr[6] == "-" or pnr[6] == "+":
            del pnr[6]
        else:
            del pnr[0]
            del pnr[0]
            del pnr[6]

        for n in pnr:
            rent_pnr += n
    else:
        rent_pnr = pnr

    return rent_pnr


def main():
    global n_number
    # Töm listorna med personnummer från gamla tester
    years.clear()

    kvinnor.clear()
    killar.clear()
    korrekta.clear()
    felaktiga.clear()

    # Öppna filen med personnummer och läs den
    file = open("numbers.txt", "r")
    numbers = file.read().splitlines()

    # Kolla igenom varje personnummer från filen
    for number in numbers:
        _number = number
        number = kolla_inputen(number)

        if number == "stop":
            pass
        elif number == "l_error":
            print("personnumret är för långt eller för kort")
        elif number == "c_error":
            print("det finns annat än siffror i talet")
        elif number == "d_error":
            print(str(_number) + " har för många dagar i månaden")
        elif number == "m_error":
            print(_number)
            print("månaden finns inte")
        else:
            algoritm(number, False)

        # Återställ år hundraden
        n_number = ["19", "20"]

    # Sortera listan med år så att det vanligaste året är först
    sorted_year = dict(sorted(years.items(), key=lambda x: x[1], reverse=True))

    print("Det var " + str(len(korrekta)) + " korrekta personnummer")
    print("Det var " + str(len(kvinnor)) + " kvinnor och " + str(len(killar)) + " killar")
    fort = input("Vill du se de korrekta? ")

    if fort == "ja":
        for n in korrekta:
            print(str(n))

    statistik = input("Vill du se statistik? ")

    if statistik == "ja":
        print("Det var " + str(round((len(korrekta) / len(numbers)) * 100, 2)) + "% som var korrekta")
        print("Det var " + str(round((len(killar) / len(numbers)) * 100, 2)) + "% som var killar")
        print("Det var " + str(round((len(kvinnor) / len(numbers)) * 100, 2)) + "% som var kvinnor")


def skriv_s(nummer):
    global n_number

    # Töm listorna med personnummer från gamla tester
    years.clear()

    kvinnor.clear()
    killar.clear()
    korrekta.clear()
    felaktiga.clear()

    try:
        nummer = kolla_inputen(nummer)
    except ValueError:
        return print("personnumret är skrivet fel")

    if nummer == "m_error":
        print("Månaden finns inte")
    elif nummer == "c_error":
        print("det finns annat än siffror i talet")
    elif nummer == "d_error":
        print("Den dagen finns inte")
    elif nummer == "y_error":
        print("Året går inte ihop med tecknet")
    elif nummer == "l_error":
        print("personnumret är för långt eller för kort")
    else:
        algoritm(nummer, True)

        n_number = ["19", "20"]
