''' index file for Flask API '''
import os
from modules.app import app
from modules import logger

if __name__ == "__main__":
    HOST = None
    _containerd = os.environ.get('FLASK_RUNNING_IN_DOCKER')
    if _containerd and _containerd == 'true':
        HOST = '0.0.0.0'

    PORT = os.environ.get('PORT')
    if PORT:
        PORT = int(PORT)
    else:
        PORT = 5001
    app.run(host=HOST, port=PORT)
