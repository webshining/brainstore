server:
	uv run python manage.py runserver 4000
telegram:
	uv run python manage.py start_bot
migrate:
	uv run python manage.py migrate
makemigrate:
	uv run python manage.py makemigrations
translate:
	uv run python manage.py makemessages -l ru & \
	uv run python manage.py makemessages -l uk & \
	uv run python manage.py makemessages -l en
compiletranslate:
	uv run python manage.py compilemessages --ignore=*.pyc --ignore=__pycache__ --ignore=venv --ignore=.venv
