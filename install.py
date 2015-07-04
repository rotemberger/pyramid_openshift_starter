__author__ = 'rotem'
import os
import sys
import subprocess

if os.geteuid() != 0:
    print('Root privilege is needed.')
    sys.exit(0)

repo_url = sys.argv[1]

# replace Pyramid Openshift starter github repository to your Openshift clean repository.
os.system('rm -rf .git')
os.system('git clone {0} os-app'.format(repo_url))
os.system('cp -r os-app/.git .git')
os.system('rm -rf os-app')
os.system('git add .')
os.system('git commit -m "Initial Pyramid Openshift starter"')
os.system('git push origin master')

# set local development environment.
os.system('pyvenv-3.4 venv')
os.system('venv/bin/pip3.4 install -r requirements.txt')
os.system('venv/bin/python3.4 setup.py develop')

dirname = os.path.dirname(os.path.abspath(__file__))
head, target_folder = os.path.split(dirname)

user = subprocess.check_output(['sh', '-c', 'echo $SUDO_USER']).strip()
os.system('chown {0} -R {1}'.format(user, dirname))

conf = None
with open('apache/st4rt3r.conf'.format(target_folder), 'r') as fh:
    conf_tmpl = fh.read()
    conf = conf_tmpl.format(target_folder, os.getcwd())

with open('/etc/apache2/sites-available/{0}.conf'.format(target_folder), 'w') as fh:
    fh.write(conf)

try:
    os.symlink('/etc/apache2/sites-available/{0}.conf'.format(target_folder),
                '/etc/apache2/sites-enabled/{0}.conf'.format(target_folder))
except OSError:
    print('symlink to sites-available already exists')


hosts = None
with open('/etc/hosts', 'r') as fh:
    hosts = fh.read()

prepend = "127.0.0.1	{0}\n".format(target_folder)
with open('/etc/hosts', 'w') as fh:
    fh.write(''.join([prepend, hosts]))

os.system('apache2ctl restart')