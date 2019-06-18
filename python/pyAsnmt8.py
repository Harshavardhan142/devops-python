import math
a = input("ENTER values of D :")
D = a.split(',')
C = 50 
H = 30
l = list()
for i in D:
    Q =  round(math.sqrt((2 * C * int(i)/H)))
    l.append(Q)

print(l)