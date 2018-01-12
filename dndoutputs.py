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
