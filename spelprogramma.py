import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']
def spelProgamma(spelList, minimum = 3, maximum = 10):
    num = random.choice(range(minimum, maximum))
    return random.choices(spelList, k=num)
print(spelProgamma(spelList))
print(spelProgamma(spelList,1))
print(spelProgamma(spelList, 1,3))