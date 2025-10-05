t2 = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin","Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
t3 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range (12):
    t2.insert( 2*i + 1 , t3[i])
print(t2)