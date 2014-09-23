from pyramid.paster import get_app, setup_logging
from os.path import dirname, abspath

ini_path = dirname(abspath(__file__)) + '/' + 'production.ini'

setup_logging(ini_path)
application = get_app(ini_path, 'main')
