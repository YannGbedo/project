from create import create;
from recup import recup;
# from verif import verif;
import sys

name = "webs1"
ip = "192.168.8.103"
user = "billy"
pwd = "billy"

args = sys.argv
name = args[1]
ip = args[2]
user = args[3]
pwd = args[4]

conn = [ip,user,pwd]

print('<br>creation du fichier')
create(name,conn)
print('<br>recuperation du fichier')
recup(name,conn)
print('<br>verification du fichier')
# verif("/var/www/html/hids/hashwebs1.txt")
print('<br>arvidersen')
