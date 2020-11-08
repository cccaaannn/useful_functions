import sys
sys.path.insert(0, "app_path")
from flask_app_path import create_app
from waitress import serve

# add logger file to waitress logger
import logging
logger = logging.getLogger("waitress")
logger.setLevel(logging.WARN)
file_handler = logging.FileHandler("waitress.log")
logger.addHandler(file_handler)

# serveing options
app = create_app()
host = "0.0.0.0"
port = 5000
threads = 5
# url_scheme = "https"

# start server
serve(app, host=host, port=port, threads=threads)