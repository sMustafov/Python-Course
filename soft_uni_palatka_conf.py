import math

peopleComing = int(input())
peopleEating = peopleComing
numberOfLines = int(input())

for i in range(0,numberOfLines):
    inputLine = str(input())
    inputLine = inputLine.split(' ')
    resource = str(inputLine[0])
    quantity = int(inputLine[1])
    type = str(inputLine[2])

    if resource == 'tent':
        if type == 'normal':
            peopleComing -= 2 * quantity
        elif type == 'firstClass':
            peopleComing -= 3 * quantity
    elif resource == 'rooms':
        if type == 'single':
            peopleComing -= quantity
        elif type == 'double':
            peopleComing -= 2 * quantity
        elif type == 'triple':
            peopleComing -= 3 * quantity
    elif resource == 'food':
        if type == 'zakuska':
            peopleEating -= 0 * quantity
        elif type == 'musaka':
            peopleEating -= 2 * quantity

if peopleComing <= 0:
    print('Everyone is happy and sleeping well. Beds left: {}'.format(int(math.fabs(peopleComing))))
else:
    print('Some people are freezing cold. Beds needed: {}'.format(int(peopleComing)))