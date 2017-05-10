# Imports all config files from config/journeychurch directory

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY
with open(os.path.join(BASE_DIR, '../config/journeychurch/SECRET_KEY')) as file:
    SECRET_KEY = file.read().strip()


# DEBUG
with open(os.path.join(BASE_DIR, '../config/journeychurch/DEBUG')) as file:
    DEBUG = file.read().strip()


# ALLOWED_HOSTS
with open(os.path.join(BASE_DIR, '../config/journeychurch/ALLOWED_HOSTS')) as file:
    ALLOWED_HOSTS = [line.strip() for line in file if not line == None]


# DATABASES
with open(os.path.join(BASE_DIR, '../config/journeychurch/DATABASE')) as file:
    DATABASE = [line.strip() for line in file if not line == None]
