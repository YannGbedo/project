import sys

fname1 = input("Entré le nom du fichier d'origine :")
fname2 = input("Entré le nom du fichier à comparé :")

f1 = open(fname1)
f2 = open(fname2)

print("---------------------")
print("Comparaison des fichiers",">" + fname1, "<" + fname2, sep='\n')
print("---------------------")

f1_line = f1.readline()
f2_line = f2.readline()

line_no = 1

while f1_line != '' or f2_line != '':

    f1_line = f1_line.rstrip()
    f2_line = f2_line.rstrip()

    if f1_line != f2_line:

        if f2_line == '' and f1_line != '':
            print(">+","Line-%d" % line_no, f1_line)

        elif f1_line != '':
            print(">", "Line-%d" % line_no, f1_line)


        if f1_line == '' and f2_line != '':
            print("<+", "Line-%d" % line_no, f2_line)

        elif f2_line != '':
            print("<", "Line-%d" % line_no, f2_line)

        print()

    f1_line = f1.readline()
    f2_line = f2.readline()

    line_no += 1

f1.close()
f2.close()
    
