from decouple import config
import os


if config('DEBUG', cast=bool) is True:
    from .settings_dev import *
else:
    from .settings_production import *
