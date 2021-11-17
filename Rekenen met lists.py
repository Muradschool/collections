listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]

def addAndDisplayLists (listOne, listTwo):
    print('--------')
    print('Add list')
    for i in range(len(listOne)):
        print(listOne[i], "+", listTwo[i], "=", listOne[i] + listTwo[i])
addAndDisplayLists(listOne, listTwo)
