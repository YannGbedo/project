import os
import paramiko
from fabric.api import *

def recup(name,conn):
	env.host_string = conn[0]
	env.user = conn[1]
	env.password = conn[2]
	get("/var/www/html/python/hash.txt","/var/www/html/hids/hash/hash"+name+".txt")
	sudo("rm -r /var/www/html/python")
