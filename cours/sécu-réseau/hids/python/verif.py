import sys

def verif(file):
    with fo = open(file, "r") as f:
        for line in f.readlines():
            user,pwd = line.split(",")
        if (len(pwd) != 64):
                print ("le fichier n'est pas conforme")
                
            i = 0
            j = 0
            while (i != len(pwd)):
                if (pwd[i] < 'a' or pwd[i] > 'z'):
                    print ("Caractère non conforme dans le mot de passe")
                elif (pwd[i] < 'A' or pwd[i] > 'Z'):
                    print ("Caractère non conforme dans le mot de passe")
                elif (pwd[i] < '0' or pwd[i] > '9'):
                    print ("Caractère non conforme dans le mot de passe")
                i+=i

            while (j != len(user)):
                if (user[j] = ';'):
                    print ("Caractère non conforme dans l' id")
                j+=j
    fo.close()
