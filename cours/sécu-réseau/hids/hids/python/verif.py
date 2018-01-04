import sys
import csv
import time

def verif(name2):
    fname1 = "../ref/"+name2
    fname2 = "../hash/"+name2
    name1 = "ref/"+name2
    name2 = "hash/"+name2
    f1 = open(fname1)
    f2 = open(fname2)

    f = open("../alert/alert.csv", 'a')
    writer = csv.writer(f)
    
    f1_line = []
    f2_line = []
    c1 = 0
    c2 = 0
    with open(fname1) as f:
        for line in f:
            f1_line.append(line)
            c1 += 1

    with open(fname2) as f:
        for line in f:
            f2_line.append(line)
            c2 += 1
        
    if c1 != c2:
        error = ['number', 'nombre de fichiers n\'est pas equivalent', name2, time.time()]
        print(error)
        writer.writerow(error)
    else:
        x = 0
        while x < c1:
            if f1_line[x] != f2_line[x]:
                lib = "not match " + str(x)
                detail = f1_line[x] + "_" + f2_line[x]
                error = [lib, detail, name2, time.time()]
                print(error)
                writer.writerow(error)
            x +=1

    f1.close()
    f2.close()