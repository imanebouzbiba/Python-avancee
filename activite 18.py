machines={
    "m1":"192.168.0.1",
    "m2":"192.168.0.2",
    "m3":"192.168.0.3",
    "m4":"192.168.0.4",
    "m5":"192.168.0.5",
}
print("l'adress IP de la machine 2 est :", machines.get("m2"))
compte=0
for key in machines:
    compte +=1
print (f"le nombre de machines dans le dictionnaire est :{compte}")
machines["m6"]="192.168.0.6"
print(machines)
del machines["m4"]
print(machines)
if "m5" in machines:
    print("la machines 5 existe sur le dictionnaire. ")
else :
    print("la machines 5 n'existe pas.")
x=input("entrez le nom de la machine :")
if x in machines:
    print(f"l'adress IP de la machine est : {machines[x]}")
else:
    print("la mahine n'est pas repertoriee.")