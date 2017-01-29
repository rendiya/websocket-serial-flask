	
from app import app

from app.controller.view import view
app.register_blueprint(view, url_prefix='/view') 

from app.controller.serial import serial
app.register_blueprint(serial, url_prefix='/serial') 