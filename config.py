import os

# Folder where the project is located
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Folder where uploaded log files will be stored
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

# Used by Flask to secure sessions
SECRET_KEY = "replace-this-with-a-random-secret-key"