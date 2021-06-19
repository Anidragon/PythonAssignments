'''
Created on Apr 6, 2021

@author: Balu
'''
f = open("grades.txt")
pokedex = f.read()

chunk = pokedex.split('\n')
CountA = 0
CountB = 0 
CountC = 0
CountD = 0
CountF = 0 
Averagetotal=0
totalnum = 0
mini = float(chunk[0]) 
print(mini)
maxi = 0 
for n in chunk:
    totalnum+=1
    Averagetotal+=float(n)
    compare = float(n)
    if compare > maxi:
        maxi = float(n)
    elif compare < mini:
        mini = float(n)
        
    if float(n) >= 90:
        CountA += 1
    elif float(n) < 90 and float(n) >= 80:
        CountB += 1
    elif float(n) < 80 and float(n) >= 70:
        CountC += 1
    elif float(n) < 70 and float(n) >= 60:
        CountD += 1
    else:
        CountF += 1
Average = Averagetotal/totalnum 
Average = round(Average, 1)  
print(CountA, CountB, CountC, CountD, CountF, Average, mini, maxi)

mini = str(mini)
maxi = str(maxi)
CountA = str(CountA)
CountB = str(CountB)
CountC = str(CountC)
CountD = str(CountD)
CountF = str(CountF)
Average = str(Average)

maxi = "Highest score" + maxi
mini = "least score:" + mini  
CountA = "A's" + CountA
CountB = "B's" + CountB
CountC = "C's" + CountC
CountD = "D's" + CountD
CountF = "F's" + CountF
Average = "Average" + Average 


G = open("grade_report.txt", "w")
G.write(mini)
G.write("\n")
G.write(maxi)
G.write("\n")
G.write(CountA)
G.write("\n")
G.write(CountB)
G.write("\n")
G.write(CountC)
G.write("\n")
G.write(CountD)
G.write("\n")
G.write(CountF)
G.write("\n")
G.write(Average)
