import hashlib
import datetime

print('ouverture du fichier')
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

mylist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890;@_#'
#mylist = 'ABC'
mylist = [i for i in mylist]

def verifhash(lehashtest,lehashadecouver):
    h = hashlib.md5()
    h.update(lehashtest.encode('utf-8'))
    lehashtest = h.hexdigest()
    if lehashtest == lehashadecouver:
        return True
    else:
        return False

def inithashtest(lenght):
    for i in range(lenght):
        hashtest.append(0)

for liste in listcomplete :
    date = datetime.datetime.now()
    print(str(date))
    hashtest=[]
    lnht=6
    inithashtest(lnht)
    lehashadecouver=liste[1]
    lehashadecouver=lehashadecouver[3:]
    modulo=0
    findhash = False
    while findhash == False:
        listlen=len(mylist)
        htlen=len(hashtest)
        MT=modulo
        i=htlen-1
        while i>=0:
            nextM=MT//listlen
            hashtest[i]=MT%listlen
            MT=nextM
            i-=1
        hts="";
        j=0
        while j<htlen:
            hts+=mylist[hashtest[j]]
            j+=1
        if verifhash(hts,lehashadecouver)==True:
            print(hts)
            print("Trouvé")
            findhash == True
            break
        
        cverif=0
        for i in range(htlen):
            if hashtest[i]==listlen-1:
                cverif+=1
        if cverif == htlen:
            hashtest=[]
            if lnht < 12:
                lnht+=1
                inithashtest(lnht)
            else:
                print("pas trouvé")
                findhash == True
        
        modulo+=1

    date = datetime.datetime.now()
    print(str(date))
    break
print('fin du programme')
shadowfile.close()

"""
def brutefct(string, length, charset):
    if len(string) == length:
        return
    for char in charset:
        temp = string + char
        h = hashlib.md5()
        h.update(temp.encode('utf-8'))
        lehashtest = h.hexdigest()
        if lehashtest == lehashadecouver:
            print(temp)
            break
        else:
            brutefct(temp, length, charset)

for liste in listcomplete :
    date = datetime.datetime.now()
    print(str(date))
    lehashadecouver=liste[1]
    compteur=6
    while compteur < 12:
        brutefct("", compteur, mylist)
    date = datetime.datetime.now()
    print(str(date))


    
for liste in listcomplete :
    lehashadecouver=liste[1]
    for current in range(6,13):
        a = [i for i in mylist]
        for y in range(current):
            a = [x+i for i in mylist for x in a]
        h = hashlib.md5()
        h.update(a.encode('utf-8'))
        lehashtest = h.hexdigest()
        if lehashtest == lehashadecouver:
            print ("j'ai trouvé le "+liste[0]+", c'est : "+a)
"""


"""
for liste in listcomplete :
    date = datetime.datetime.now()
    print(str(date))
    hashtest=[]
    inithashtest(6)
    lehashadecouver=liste[1]
    findhash = False
    
    while findhash == False:
        i=0
        listlen=len(mylist)
        htlen=len(hashtest)
        while i<listlen:
            hts="";
            hashtest[htlen-1]=i
            j=0
            while j<htlen:
                hts+=mylist[hashtest[j]]
                #if verifhash(hts,lehashadecouver)==True:
                j+=1
            print(hts)
            i+=1
        hashtest[htlen-2]+=1
        cverif=0
        for i in range(htlen):
            if hashtest[i]==htlen:
                cverif+=1
        if cverif == htlen:
            hashtest=[]
            inithashtest(7)
    date = datetime.datetime.now()
    print(str(date))
"""

