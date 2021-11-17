listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]
def addAndDisplayLists (listOne, listTwo):
    print('--------')
    print('Add list')
    for i in range(len(listOne)):
        print(listOne[i], "+", listTwo[i], "=", listOne[i] + listTwo[i])
addAndDisplayLists(listOne, listTwo)
def substractAndDisplayLists (listOne, listTwo):
    print('---------')
    print('Substract List')
    for i in range(len(listOne)):
        print(listOne[i], "-", listTwo[i], "=", listOne[i] - listTwo[i])
substractAndDisplayLists(listOne, listTwo)
def multiplyAndDisplayLists (listOne, listTwo):
    print('---------')
    print('Multiply List')
    for i in range(len(listOne)):
        print(listOne[i], "*", listTwo[i], "=", listOne[i] * listTwo[i])
multiplyAndDisplayLists(listOne, listTwo)
def divideAndDisplayLists (listOne, listTwo):
    print('---------')
    print('Divide List')
    for i in range(len(listOne)):
        print(listOne[i], '/', listTwo[i], '=', listOne[i] / listTwo[i])
divideAndDisplayLists(listOne, listTwo)