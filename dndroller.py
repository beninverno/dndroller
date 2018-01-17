from dndoutputs import *

def main():
    monsterdict = {}
    askforinput = True
    newround = True
    while askforinput == True:
        name = str(input('What is the name of the Monster?: '))
        initmod = str(input('What is the initiative modifier of the monster?: '))
        atk = 'd20'
        atkmod = str(input('What is the modifier of the attack roll? (+2, -3, etc.): '))
        dmg = str(input("What is the dice roll of the damage?: "))
        dmgmod = str(input('What is the modifier of the damage roll?: '))
        quantity = int(input('How many of these monsters would you like to put in?: '))
        sameinit = bool(int(input('Would you like to have the multiple monsters at same initiative? (1 for True, 0 for False): ')))
        monsterdict = populatedictwithinfo(name, initmod, atk, atkmod, dmg, dmgmod, quantity, sameinit, monsterdict)
        tocontinue = bool(int(input('Would you like to add another monster? (1 for True, 0 for False): ')))
        print("")
        if tocontinue == True:
            continue
        if tocontinue == False:
            askforinput = False
    while newround == True:
        printInitiative(monsterdict)
        newround = bool(int(input('Roll for a new round? (1 for True, 0 for False): ')))
        if newround == True:
            monsterdict = updatedict(atk, atkmod, dmg, dmgmod, monsterdict)
            
def populatedictwithinfo(name, initmod, atk, atkmod, dmg, dmgmod, quantity, sameinit, monsterdict):
    initiative = calculateattack('d20', initmod)
    for i in range(quantity):
        if sameinit != True:
            initiative = calculateattack('d20', initmod)
        attackroll = calculateattack(atk, atkmod)
        damageroll = calculateattack(dmg, dmgmod)
        newname = name + ' ' + str(i + 1)
        monsterdict[newname] = [initiative, attackroll, damageroll]
    return monsterdict

def updatedict(atk, atkmod, dmg, dmgmod, monsterdict):
    for values in monsterdict:
        monsterdict[values] = [monsterdict[values][0], calculateattack(atk, atkmod), calculateattack(dmg, dmgmod)]
    return monsterdict
                            
                        

        
if __name__ == "__main__":
    main()


