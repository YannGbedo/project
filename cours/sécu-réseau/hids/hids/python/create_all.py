import hashlib
import os
import sys

args = sys.argv
name = args[1]
path ='/var/www/html/'+name

f = open("/var/www/html/python/hash.txt", "w")
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
        #print(hasher.hexdigest())
        f.write("\n")
f.close