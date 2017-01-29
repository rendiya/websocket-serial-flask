install all requirement

pip install -r requirement.txt (need super user)

run server with gevent socketio worker

gunicorn --worker-class socketio.sgunicorn.GeventSocketIOWorker main:app -b 127.0.0.1:5000

open in your browser

localhost:5000/serial

to change your configuration, please change in config.json
