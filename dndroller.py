from dndoutputs import *

monsterdict = {}

def main():
    while True:
        name = str(input('What is the name of the Monster?: '))
        initmod = str(input('What is the initiative modifier of the monster?: '))
        atk = str(input('What is the dice roll of the attack? (d20, d10, d12, etc.): '))
        atkmod = str(input('What is the modifier of the attack roll? (+2, -3, etc.): '))
        dmg = str(input("What is the dice roll of the damage?: "))
        dmgmod = str(input('What is the modifier of the damage roll?: '))
        quantity = int(input('How many of these monsters would you like to put in?: '))
        sameinit = bool(int(input('Would you like to have the multiple monsters at same initiate? (1 for True, 0 for False): ')))
        populatedictwithinfo(name, initmod, atk, atkmod, dmg, dmgmod, quantity, sameinit)
        print(monsterdict)
        break

def populatedictwithinfo(name, initmod, atk, atkmod, dmg, dmgmod, quantity, sameinit):
    initiative = calculateattack('d20', initmod)
    for i in range(quantity):
        if sameinit != True:
            initiative = calculateattack('d20', initmod)
        attackroll = calculateattack(atk, atkmod)
        damageroll = calculateattack(dmg, dmgmod)
        newname = name + ' ' + str(i)
        monsterdict[newname] = [initiative, attackroll, damageroll]

if __name__ == "__main__":
    main()


