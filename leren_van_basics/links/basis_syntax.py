


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


def main():
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
    dict()

if __name__ == "__main__":
    main()


def dict():
    dict = [0,5,9]
    print(dict.append(1))