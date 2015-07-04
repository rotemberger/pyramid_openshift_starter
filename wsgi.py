import os
import sys

BASE_DIR = os.path.dirname(__file__)
ini_path = os.path.join(BASE_DIR, 'production.ini')

# add venv to develop on local machine.
venv_site_packages_dir = os.path.join(BASE_DIR, 'venv/lib/python3.4/site-packages')
if venv_site_packages_dir not in sys.path:
    sys.path.append(venv_site_packages_dir)

from pyramid.paster import get_app, setup_logging

setup_logging(ini_path)
application = get_app(ini_path, 'main')
