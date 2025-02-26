import sys
path = '/var/www/webroot/ROOT'
if path not in sys.path:
    sys.path.append(path)
from main import app
application = app