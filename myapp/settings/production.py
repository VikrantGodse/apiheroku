import os
import json
import dj_database_url

SECRET_KEY = 'cc1l4=)oyi7l$j*9_+1m*+pz6!01#n#5oe)%wabf5$nvyfy(+f'

DEBUG = False

connection = dj_database_url.parse(os.environ.get("DATABASE_URL"))
connection.update({
    'CONN_MAX_AGE': 600,
})
DATABASES = {
    "default": connection,
}

ALLOWED_HOSTS = [os.environ.get("HOST", "*"), ]
