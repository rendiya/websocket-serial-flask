from flask import Blueprint, render_template, abort,request,Response
import json

serial = Blueprint('modul_serial', __name__,template_folder='templates')

from flask.ext.socketio import SocketIO, emit
import random
import time
from threading import Thread, Event
import string
from app import app
from app.model.serial_conn import Serializer
from app.config import test_port

#turn the flask app into a socketio app
socketio = SocketIO(app)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()
#test_port = Serializer(port = '/dev/ttyACM0',baudrate=9600,waiting=True)

class RandomThread(Thread):
    def __init__(self):
        self.delay = 1
        super(RandomThread, self).__init__()

    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """

        #infinite loop of magical random numbers
        while not thread_stop_event.isSet():
            #if test_port.in_waiting:
            try:
                serial_py = test_port.recv()
                socketio.emit('newnumber', {'number2': serial_py}, namespace='/test')
                time.sleep(1)

            except Exception as e:
                print e
                pass

    def run(self):
        self.randomNumberGenerator()

@serial.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    #return "hello"
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')
    #socketio.emit('newnumber', {'number2': 23}, namespace='/test')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print "Starting Thread"
        thread = RandomThread()
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

@socketio.on('value changed',namespace='/test')
def value_changed(message):
    #values[message['who']] = message['data']
    #emit('update value', message, broadcast=True)
    print message
    #try:
    test_port.send(msg=str(message['data']))
#    except Exception as e:
#        print e
