import random

HoeveelheidMenM = int(input("Hoeveel M&M's moet er worden toegevoegd aan de zak?\n"))

Kleur = ["oranje", "blauw", "groen", "bruin"]

MnmZak = {}

def MenM(amount): 
    for i in range(amount):
        randomColor = random.choice(Kleur)
        if randomColor in MnmZak:

            MnmZak[randomColor] += 1
        else:

            MnmZak.update({randomColor : 1})

    return MnmZak
print(sorted(MenM(HoeveelheidMenM).items()))
