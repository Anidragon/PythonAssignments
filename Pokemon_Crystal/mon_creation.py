'''
Created on Mar 31, 2021

@author: Balu
'''
import random
f = open("Pokemon Essentials v18.1 2020-09-28/PBS/pokemon.txt", 'r', encoding='utf-8')
pokedex = f.read()


HPIv = random.randint(-1,31)

AtkIv = random.randint(-1,31)
 
DefIv = random.randint(-1,31)
 
SpAtkIv = random.randint(-1,31)
 
SpDefIv = random.randint(-1,31)
 

def Mon_create(Name, HPIv, AtkIv, DefIv, SpAtkIv, SpDefIv, Nature, Move1, Move2, Move3, Move4, lvl, Ability, Nature):
    print(Name)
    print("____________")
    
    