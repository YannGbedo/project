from create import create;
from recup import recup;
from verif import verif;

conn = ["192.168.8.200","billy","billy"]

create('/var/www/html/wordpress')
recup(conn)
verif("/var/www/html/webs/hash1.txt")
