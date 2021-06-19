'''
Created on Mar 29, 2021

@author: Balu
'''

import random
crit_chance = random.randint(0,100)
if crit_chance <= 6:
    crit = True
else:
    crit = False    
R = random.randint(-1, 15)
Rtop = 85 + R 
random = Rtop/100
TE = 1
STAB = 1.5
O = 1
Mod = STAB * random * TE * O


def damage_calc(Lvl, AtkStat, DefStat, BasePower, Mod ):
    if crit == True:
        Lvl = Lvl*2
    else:
        Lvl = Lvl
    dtop = 2*Lvl + 10
    d1 = dtop / 250
    d2 = AtkStat/DefStat
    d3 = d1 + d2
    d4 = d3 * BasePower + 2
    damage = d4*Mod
    return round(damage,0)
    



print(damage_calc(50, 65, 65, 55, Mod))
print(damage_calc(100, 169, 129, 90, 1.5))