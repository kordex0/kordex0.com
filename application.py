"""
This file is used by aws to start up the application
"""


from pyramid.paster import get_app, setup_logging
import os.path

ini_path = os.path.join(os.path.dirname(__file__), 'development.ini')
setup_logging(ini_path)
application = get_app(ini_path, 'main')