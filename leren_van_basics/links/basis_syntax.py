from time import sleep
import random
import csv

# def main():
#     eerste_vraag = int(input("Hallo, hoe oud bent je?"))
#     if eerste_vraag <= 18:
#         te_jong = print("Je bent te jong")
#     else:
#         oud_genoeg = print("Fijn, je mag naar binnen")
#     if eerste_vraag <= 18:
#         len(te_jong)
#     else:
#         len(oud_genoeg)
#     except ValueError:
#             print("Voer een getal in")
#
#     print(type(eerste_vraag))
#
#
#
#
# if __name__ == "__main__":
#     main()
def narmalna():
    try:
        eerste_vraag = int(input("Hallo, hoe oud bent je?"))
        if eerste_vraag <= 18:
            te_jong = "Je bent te jong"
            print(te_jong)
            print(("karakters:", len(te_jong)))
        else:
            oud_genoeg = "Fijn, je mag naar binnen"
            print(oud_genoeg)
            print("karakters", len(oud_genoeg))
    except ValueError:
        print("Voer een getal in.")


def vraag():
    while True:
        try:
            vapros = int(input("Hoe oud bent je?"))
            if vapros <= 18:
                print("Te jong, kom als je ouder bent.")
                sleep(3)
            elif vapros >= 18:
                print("Kom binnen.")
                sleep(5)
            return
            sleep(3)
        except ValueError:
            print("Voer een getal in.")


def dictie():
    dictio = {'a': 0, 'b': 5, 'c': 9, 'd': 1, 'e': 2, 'f': 10, 'g': 25}
    with open("pravda", 'w', newline='') as bestand:
        schrijver = csv.writer(bestand)
        for letter, cijfer in dictio.items():
            item = random.choice(list(dictio))
            schrijver.writerow([letter, cijfer])
            print(letter, cijfer)
            del dictio[item]
            sleep(3)

def main():

    dictie()
    vraag()

if __name__ == "__main__":
    main()

