DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "/home/alan/coding/shoutcast-web/shoutcast/dev.db",                       # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

ECHOES_NEST_API_KEY = "6ELTPYPVXF11BNXV0"
MUSIC_STORAGE_PATH = "/home/alan/Music"
MUSIC_URL = "http://localhost/"
MUSIC_PATHS = []
API_URL = "http://localhost:7999"
API_USER = "admin"
API_PASS = "goaway"