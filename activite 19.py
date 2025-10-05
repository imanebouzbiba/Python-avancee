#fonction F1
def F1(n):
    for i in range(n):
        print("Bonjour")
print(F1(5))

#fonction F2
def F2(n):
    if n%10 == 0 :
        print(f"la valeur {n} est divisible par 10.")
    else:
        print(f"la valeur {n} n'est pas divisible par 10.")
print (F2(60))
print(F2(22))

#fonction F4
def F4(n):
    if n < 0 :
        return " le factorielle n'existe pas pour les valeurs negatives."
    elif n == 0 or n == 1 :
        return 1
    else:
        return n * F4(n- 1)
print(F4(0))
print(F4(5))
print(F4(-5))

#fonction F3
def F3(mots):
    compte=0
    voyelles = ['a','i','e','u','o','y']
    for i in mots :
       if i in voyelles:
           compte+=1
    return compte
print(F3("imane")) 

#fonction F5
def F5(n):
    for i in range (1 , 11 ):
        a= i*n
        print (f"{i} x {n} = {a}")
print(F5(7))
print(F5(4))

# fonction F6
def F6(mots):
    compte=0
    for i in mots:
        compte+=1
    return compte
print(F6("imane"))

#fonction F7
def F7(n):
    if n ==0 :
        return 0
    elif n==1:
        return 1
    else:
        return F7(n-1)+F7(n-2)
print(F7(2))
print(F7(0))
print(F7(6))