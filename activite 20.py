adresses_ip=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]
print("1.la premier adress dans la liste est :", adresses_ip[0])
print("2.la dernier adess dans la liste est :", adresses_ip[-1])
print("3.la troisieme adress dans liste est :", adresses_ip[2])
adresses_ip.append("172.31.0.1")
print("4.",adresses_ip)
adresses_ip.remove("200.100.50.1")
print("5.",adresses_ip)
x= len(adresses_ip)
print(f"6.le nombres d'adress restants dans la liste apres les modification est:{x}")
if "192.168.0.1" in adresses_ip:
    print ("7.l'adresse 192.168.0.1 existe dans la listes.")
else:
    print ("7.l'adresse 192.168.0.1 n'existe pas dans la listes.")
#la classe de l'adress depend de la premier partie de l'adress
ip="10.0.0.1" 
prmier_octet = int(ip.split(".")[0]) # on prend la pemier partie de l'adress 
if 1 <= prmier_octet <= 126 :
    classe ="A"
elif 128 <= prmier_octet <= 191 :
    classe = "B"
elif 192 <= prmier_octet <=191:
    classe="c"
else:
    classe="Autre"
print("8.la classe de l'adress '10.0.0.1'est :",classe)
adresses_ip.sort() # trie l'adress IP par ordre alphabetique
print("9.liste trie par ordre croissant ", adresses_ip)
compteur = 0
for i in adresses_ip:
    prmier_octet = int(ip.split(".")[0]) # on prend la pemier partie de l'adress 
    if 192 <= prmier_octet <= 223 :
        compteur+=1
if compteur == len (adresses_ip) :
    print ("10.tous les adresse sont de class C.")
else:
    print("10.qlq adresses sont pas de class C.")

compteur_publique = 0  

for i in adresses_ip:
    # On sépare les nombres de l’adresse IP (ex: "192.168.0.1" → [192,168,0,1])
    p = list(map(int, ip.split(".")))
    # On teste les cas d'adresses NON publiques
    if p[0] == 10:                 # 10.x.x.x → privé
        continue
    elif p[0] == 172 and 16 <= p[1] <= 31:  # 172.16.x.x → 172.31.x.x → privé
        continue
    elif p[0] == 192 and p[1] == 168:       # 192.168.x.x → privé
        continue
    elif p[0] == 169 and p[1] == 254:       # 169.254.x.x → lien local
        continue
    else:
        # Si ce n’est aucun de ces cas → c’est public
        compteur_publique += 1

print("11. Nombre d’adresses IP publiques :", compteur_publique) 
