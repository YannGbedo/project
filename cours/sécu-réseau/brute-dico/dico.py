import hashlib
import datetime

print('ouverture du fichier shadow')
shadowfile=open("shadow", "r")
contenu=shadowfile.read()
chaine = contenu.split(":")
chainemax=len(chaine)
listcomplete=[]
liste=[]
y=0
for value in chaine:
    liste.append(value)
    y+=1
    if(y>7):
        listcomplete.append(liste)
        liste=[]
        y=0

for liste in listcomplete :
    date = datetime.datetime.now()
    print(str(date))
    lehashadecouver=liste[1]
    lehashadecouver=lehashadecouver[3:]
    print('ouverture du dico')
    ledico=open("dico_mini_fr", "r")
    ledico=ledico.read()
    dico = ledico.split("\n")
    dicomax=len(dico)
    for mdp in dico:
        h = hashlib.md5()
        h.update(mdp.encode('utf-8'))
        lehashtest = h.hexdigest()
        if lehashtest == lehashadecouver:
            print(mdp)
            break
    
    date = datetime.datetime.now()
    print(str(date))

print('fin du programme')
shadowfile.close()
