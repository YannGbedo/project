import sys

def checkhash(file):
    with open(file, "r") as f:
        for line in f.readlines():
            user,pwd = line.split(",")
        if (len(pwd) != 64 or pwd.count(' ') != 0 or pwd.count(';') != 0):
            print ("le fichier n'est pas conforme")
        if (user.count(';') != 0 or user.count(' ') != 0):
            print ("Caractère non conforme dans l'id")

            
