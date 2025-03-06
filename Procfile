Procfile

web: gunicorn todo_app.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn todo_app.wsgi


runtime.txt
python --version

requirements.txt
django
gunicorn
whitenoise


settings.py
 'whitenoise.middleware.WhiteNoiseMiddleware',
STATICSTORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CSRF_TRUSTED_ORIGINS= [""]
