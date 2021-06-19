'''
Created on Mar 14, 2021

@author: Balu
'''

import random

players = ["ani", "anushka", "kavin","ksheera" ]

random.shuffle(players)

group1 = players[0:1]
group2 = players[2:0]

combined = zip(group1, group2)

for first_student, second_student in combined:
    print(str(first_student), "and", str(second_student))   
    
    
    