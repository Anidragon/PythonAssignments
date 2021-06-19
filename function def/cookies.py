'''
Created on Apr 14, 2021

@author: Balu
'''

cookiefile = open('cookie_order.txt', 'r')

cookie_list = [0,0,0,0]
for l in cookiefile:
    l = l.rstrip()
    if l == 'Thin Mints':
        cookie_list[0]+=1
    elif l == 'Thanks-A-Lots':
        cookie_list[1]+=1
    elif l == 'Peanut Butter Patties':
        cookie_list[2]+=1
    else:
        cookie_list[3]+=1


c1 = "Thin Mints:" + str(cookie_list[0])
c2 = "Thanks-A-Lots:" + str(cookie_list[1])
c3 = "Peanut Butter Patties:" + str(cookie_list[2])
c4 = "Lemonades:" + str(cookie_list[3])
total = "total:" + str(cookie_list[0] + cookie_list[1] + cookie_list[2] + cookie_list[3])
finalsheet = open('cookie_count.txt', 'w')
finalsheet.write(c1)
finalsheet.write('\n') 
finalsheet.write(c2) 
finalsheet.write('\n') 
finalsheet.write(c3) 
finalsheet.write('\n') 
finalsheet.write(c4) 
finalsheet.write('\n')
finalsheet.write(total)      
