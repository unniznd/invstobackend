
from pathlib import Path

import os
import json

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get("SECRET_KEY")


ALLOWED_HOSTS = ['invstobackend.herokuapp.com']


with open('secret_key.json') as f:
    secret = json.load(f)

DATABASES = {
    "default": {
        "ENGINE": secret['ENGINE'],
        "NAME": secret['NAME'],
        "USER": secret['USER'],
        "PASSWORD":os.environ.get('PASSWORD'),
        "HOST":secret['HOST'],
        "PORT": secret['PORT']
    }
}
