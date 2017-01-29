#from flask import Flask,abort
from flask import *
import json
from datetime import timedelta
import config
#from app.model import serial_conn
app = Flask(__name__)

import route
import abort