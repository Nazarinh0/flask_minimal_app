run_dev:
	env FLASK_APP=hello_world.py \
	FLASK_DEBUG=1 \
	python3.10 -m flask run

run:
	gunicorn --workers=4 --bind=127.0.0.1:5000 hello_world:app
