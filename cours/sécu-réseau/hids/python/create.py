#create file and write hash into it. maybe with id ?

import hashlib
import os

def verif(path):
    f = open("hash.txt", "a+")
    BLOCKSIZE = 60000
    hasher = hashlib.sha256()

    #go through every file in the wordpress
    for root, dirs, files in os.walk(path):
        for file in files:
            with open(os.path.join(root, file), 'rb') as dbfile:
                buffer = dbfile.read(BLOCKSIZE)
                while len(buffer) > 0:
                    hasher.update(buffer)
                    buffer = dbfile.read(BLOCKSIZE)
            f.write(hasher.hexdigest())
            print(hasher.hexdigest())
            f.write("\n")
    f.close
