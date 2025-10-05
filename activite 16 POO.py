import math
L3=[1,2,3,4,5]
for val in L3 :
    print(val)
somme = sum(L3)
print("La somme est :", somme)
a = L3[2]  
b = L3[4]  
# Sélectionner les valeurs comprises dans l'intervalle [a, b]
valeurs_dans_intervalle = [x for x in L3 if a <= x <= b]
# Calculer le produit
produit = math.prod(valeurs_dans_intervalle)
print("Les valeurs dans l'intervalle :", valeurs_dans_intervalle)
print("Produit des valeurs :", produit)
maximum = max(L3)
minimum = min(L3)
print("Maximum :", maximum)
print("Minimum :", minimum)
count_multiples_3 = sum(1 for x in L3 if x % 3 == 0)
print("Nombre de multiples de 3 :", count_multiples_3)
L3.reverse()
print("Liste inversée :", L3)

