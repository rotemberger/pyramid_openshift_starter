import os
from pyramid.paster import get_app, setup_logging

BASE_DIR = os.path.dirname(__file__)

ini_path = os.path.join(BASE_DIR, 'production.ini')

setup_logging(ini_path)

application = get_app(ini_path, 'main')
