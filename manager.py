import sys
import perssonnummer
import generator


def main():
    vad = input("Vad vill du göra? ")

    if vad == "gen":
        antal = int(input("Hur många nummer vill du generera? "))

        generator.change_antal(antal)
        generator.start_gen()
    elif vad == "kolla":
        perssonnummer.main()
    elif vad == "exit":
        sys.exit()
    else:
        perssonnummer.skriv_s(vad)


while True:
    main()
