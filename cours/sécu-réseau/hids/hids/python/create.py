import os
import paramiko
from fabric.api import *

def create(name,conn):
	env.host_string = conn[0]
	env.user = conn[1]
	env.password = conn[2]
	run("mkdir /var/www/html/python")
	put('/var/www/html/hids/python/create_all.py','/var/www/html/python/create_all.py')
	run('python /var/www/html/python/create_all.py '+name+'')
