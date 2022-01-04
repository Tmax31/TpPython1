import re

def calcul_age(annee):
    return 2022 - annee

def verif_mail(adresse):
    rex = re.compile("[A-Za-z0-9]{30}@[A-Za-z0-9]{10}\.[A-Z|a-z]{3}")
    if rex.fullmatch(adresse):
        return True
    else:
        return False

def verif_mail_long(adresse):
    if adresse[4] != "@" or adresse[11] != ".":
        return False
    for ind, val in enumerate(adresse):
        if (ind < 4) or (ind >= 5 and ind <= 10) or ind > 11:
            if not val.isalnum():
                return False
    return True

continuer = True
while continuer:
    nom = input("indiquez votre nom\n")
    prenom = input("indiquez votre prenom\n")
    year = input("indiquez votre année de naissance\n")
    mail = input("indiquez votre adresse mail\n")
    try:
        year = int(year)
    except ValueError:
        print("veuillez indiquer l'année en chiffres")
    else:
        continuer = False

    if year > 2016:
        print("Vous ne pouvez pas etres admis car vous avez moins de 6ans\n")
    elif year < 2016 and year > 2010:
        print("Vous etes admis en Poussin\n")
        print(f"{nom} {prenom} née en {year} est admis en junior\nadresse mail {mail}\n")
    elif year < 2010 and year > 2002:
        print("Vous etes admis en Cadet\n")
        print(f"{nom} {prenom} née en {year} est admis en junior\nadresse mail {mail}\n")
    elif year < 2002 and year > 1998:
        print("Vous etes admis en Junior\n")
        print(f"{nom} {prenom} née en {year} est admis en junior\nadresse mail {mail}\n")
    elif year < 1998 and year > 1992:
        print("Vous etes admis en Semi-pro\n")
        print(f"{nom} {prenom} née en {year} est admis en semi-pro\nadresse mail {mail}\n")
    elif year < 1992 and year == 1982:
        print("Vous etes admis en pro\n")
        print(f"{nom} {prenom} née en {year} est admis en pro\nadresse mail {mail}\n")
    elif year < 1982:
        print("Vous ne pouvez pas etres admis car vous avez plus de 40ans\n ")
        print(f"{nom} {prenom} née en {year} n'est pas admis\nadresse mail {mail}\n")







mail = input("indiquez votre adresse mail\n")

if verif_mail_long(mail):
    print("OK")
else:
    print("KO")
