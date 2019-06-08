export FLASK_APP=run.py

flask db upgrade

export ENABLE_SCHEDULING=1
uwsgi uwsgi.ini
