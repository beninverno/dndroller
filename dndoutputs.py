import random

def rolldice(dicenum):
    return random.randrange(1, dicenum + 1)

def calculateattack(dicetoroll, modifier):
    dicenum = int(dicetoroll[1:])
    if modifier[0] == '+':
        modifier = int(modifier[1:])
    else:
        modifier = int(modifier)
    dice = rolldice(dicenum)
    if dice + modifier < 1:
        return 1
    else:
        return dice + modifier

def printInitiative(monsterdict):
    listToPrint = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20]]
    for name in monsterdict:
        init = monsterdict[name][0]
        if init > 20:
            init = 20
        monsterdict[name][0] = name
        if name not in listToPrint[init]:
            for items in monsterdict[name]:
                listToPrint[init].append(items)
        else:
            for i in range(3):
                listToPrint[init][i] += monsterdict[name][i]
        monsterdict[name][0] = init
    print('  Initiative  |     Name     |  Attack Roll |  Damage Roll |')
    print('--------------|--------------|--------------|--------------|')
    for lists in reversed(listToPrint):
        inittoprint = str(lists[0])
        print((" " * 6) + inittoprint + (" " * (8 - len(inittoprint))) + '|', end = "")
        if len(lists) > 1:
            for i in range(1, len(lists)):
                if (i - 1) % 3 == 0 and i != 1:
                    print("")
                    print((" " * 14) + "|", end = "")
                toprint = str(lists[i])
                length = len(toprint)
                firstspace = (14 - length) // 2
                secondspace = (14 - length) // 2
                while firstspace + secondspace + length != 14:
                    secondspace += 1
                print((" " * firstspace) + toprint + (" " * secondspace) + "|", end = "")
                if i == len(lists) - 1:
                    print("")
        else:
            print((" " * 14) + "|" + (" " * 14) + "|" + (" " * 14) + "|")
    print('--------------|--------------|--------------|--------------|')
