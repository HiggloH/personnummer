import matplotlib.pyplot as plt

running = True

n_number = ["19", "20"]
#Då är det 1900-talet
n_span = [25, 99]
m_nummer = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
#Max antal dager per månad, februari har två max antal beroende på om det är skottår
dagar = [31, 28, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Två listor för felaktiga och korrekta personnummer
korrekta = []
felaktiga = []

#Listor för könen
killar = []
kvinnor = []

#För att logga födelseåren
years = {}


def algoritm(nummer, p: bool):
    nummer_list = list(nummer)

    #Kolla om personnumret är för kort
    if len(nummer_list) < 10:
        return print("Personnummer är för kort")
    elif len(nummer_list) > 10:
        return print("Person numret är för långt")
    else:
        #Gör om att element i personnumret till heltal
        for s in range(len(nummer_list)):
            nummer_list[s] = int(nummer_list[s])

        kolla_kon(nummer_list)

        sum_list = []

        #Gör Luhn-algoritmen för att kolla om personnumret är korrekt eller inte
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

        #Kolla om summan från luhn algoritm är delbar med tio, då är det ett korrekt personnummer
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


def kolla_nn_mm_dd(_input) -> str:
    _input_list = list(_input)

    #Hitta året, månaden och dagen från person numret
    nn = _input_list[0] + _input_list[1]
    mm = _input_list[2] + _input_list[3]
    dd = _input_list[4] + _input_list[5]

    #Kolla om vilket år hundred det är
    if n_span[0] <= int(nn) <= n_span[1]:
        nn = n_number[0] + nn
    else:
        nn = n_number[1] + nn

    if nn in years:
        value = years[nn] + 1
        years[nn] = value
    else:
        years[nn] = 1

    #kolla om det är ett skottår
    skott = (int(nn) % 4) == 0
    if int(nn) % 100 == 0:
        if int(nn) % 400 == 0:
            skott = True
        else:
            skott = False

    #Kolla så att månaden är finns
    try:
        mm_nummer = m_nummer.index(mm) + 1
    except ValueError:
        return "m_error"

    if mm_nummer == 1:
        mm_nummer = 0

    #Så att mm_nummer matchar med dagar listan
    #Om det är februari annars spelar det ingen roll om det är skottår eller inte
    if mm_nummer == 2 and skott:
        mm_nummer = 2
    elif mm_nummer == 2 and not skott:
        mm_nummer = 1

    #Ta antalet dagar i månaden från en lista med antalet dagar för varje månad
    max_dagar = dagar[mm_nummer]

    #Kolla så att dagen finns i månaden
    if 1 <= int(dd) <= max_dagar:
        pass
    else:
        return "d_error"

    return _input


def kolla_inputen(_input) -> str:
    global n_number
    _input_list = list(str(_input))

    #Se till så att inte inputen är tom
    if len(_input_list) == 0:
        return "stop"

    index = []
    gammal = False

    #Kolla om personen är över hundra år
    try:
        _input_list.index("-")
    except ValueError:
        try:
            _input_list.index("+")
            gammal = True
        except ValueError:
            yy = _input_list[0] + _input_list[1]

            if str(yy) == "20":
                del _input_list[0]
                del _input_list[0]
            elif str(yy) == "19" or str(yy) == "18":
                y = _input_list[2] + _input_list[3]

                if 25 > int(y) >= 00:
                    gammal = True

                del _input_list[0]
                del _input_list[0]

            else:
                if 25 > int(yy) >= 00:
                    gammal = True

    #Gör om år hundraderna för om man är över hundra år
    if gammal:
        n_number = ["18", "19"]

    #Ta bort tecken som inte är bokstäver
    for tal in range(len(_input_list)):
        try:
            int(_input_list[tal])
        except ValueError:
            index.append(tal)

    #Vänd index listan för att börja från det största indexen
    index.reverse()

    #Ta bort talen från första listan
    for n in index:
        del _input_list[n]

    ny_input = ""

    #Gör om listan med alla tecken i personnumret till en sträng
    for num in _input_list:
        ny_input += num

    ny_input = kolla_nn_mm_dd(ny_input)

    return ny_input


def main():
    global n_number
    #Töm listorna med personnummer från gamla tester
    years.clear()

    kvinnor.clear()
    killar.clear()
    korrekta.clear()
    felaktiga.clear()

    #Öppna filen med personnummer och läs den
    file = open("numbers.txt", "r")
    numbers = file.read().splitlines()

    #Kolla igenom varje personnummer från filen
    for number in numbers:
        _number = number
        number = kolla_inputen(number)

        if number == "stop":
            pass
        elif number == "d_error":
            print(str(_number) + " har för många dagar i månaden")
        elif number == "m_error":
            print(_number)
            print("månaden finns inte")
        else:
            algoritm(number, False)

        #Återställ år hundraden
        n_number = ["19", "20"]

    #Sortera listan med år så att det vanligaste året är först
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
        #get_y(sorted_year)


def get_y(_years):
    x_axis = list(_years.keys())
    y_axis = list(_years.values())

    plt.scatter(x_axis, y_axis)

    plt.show()


def skriv_s(nummer):
    #Töm listorna med personnummer från gamla tester
    years.clear()

    kvinnor.clear()
    killar.clear()
    korrekta.clear()
    felaktiga.clear()

    nummer = kolla_inputen(nummer)

    if nummer == "m_error":
        print("Månaden finns inte")
    elif nummer == "d_error":
        print("Det datumet finns inte")
    elif nummer == "sn_error":
        print("Du är för gammal")
    elif nummer == "bn_error":
        print("Du är inte född en")
    elif nummer == "minus_error":
        print("Det fattas ett - eller + tecken innan de fyra sista siffrorna")
    else:
        algoritm(nummer, True)
