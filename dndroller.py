from dndoutputs import *

monsterdict = {}

def main():
    while True:
        name = str(input('What is the name of the Monster?: '))
        initmod = str(input('What is the initiative modifier of the monster?: '))
        atk = 'd20'
        atkmod = str(input('What is the modifier of the attack roll? (+2, -3, etc.): '))
        dmg = str(input("What is the dice roll of the damage?: "))
        dmgmod = str(input('What is the modifier of the damage roll?: '))
        quantity = int(input('How many of these monsters would you like to put in?: '))
        sameinit = bool(int(input('Would you like to have the multiple monsters at same initiative? (1 for True, 0 for False): ')))
        populatedictwithinfo(name, initmod, atk, atkmod, dmg, dmgmod, quantity, sameinit)
        tocontinue = bool(int(input('Would you like to add another monster? (1 for True, 0 for False): ')))
        if tocontinue == True:
            continue
        if tocontinue == False:
            printInitiative(monsterdict)
            break

def populatedictwithinfo(name, initmod, atk, atkmod, dmg, dmgmod, quantity, sameinit):
    initiative = calculateattack('d20', initmod)
    for i in range(quantity):
        if sameinit != True:
            initiative = calculateattack('d20', initmod)
        attackroll = calculateattack(atk, atkmod)
        damageroll = calculateattack(dmg, dmgmod)
        newname = name + ' ' + str(i + 1)
        monsterdict[newname] = [initiative, attackroll, damageroll]

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
    print('  Initiative  |     Name     |  Attack Roll |  Damage Roll |')
    print('--------------|--------------|--------------|--------------|')
    for lists in listToPrint:
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

if __name__ == "__main__":
    main()


