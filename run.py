from app import app
from config import config

PORT = config['port']
DEBUG = config['debug']

if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
