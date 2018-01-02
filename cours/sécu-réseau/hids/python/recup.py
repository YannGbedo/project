import os
import paramiko
from fabric.api import *

def recup(conn):
	env.host_string = conn[0]
	env.user = conn[1]
	env.password = conn[2]
	get("/var/www/html/webs1/hash.txt","/var/www/html/webs/hash1.txt")

