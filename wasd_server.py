#!/usr/bin/python

from pyfirmata import Arduino
from pyfirmata import SERVO
from time import sleep
from os import popen
import piface.pfio as pfio

from threading import Timer
from time import time

from flask import Flask, Response
app = Flask(__name__)


board = Arduino('/dev/ttyUSB0')
pfio.init()

sleep(2)
Ptilt = 2
Ppan = 4

LeftForward = 3
LeftBack = 11
RightBack = 5
RightForward = 6

light = False

pan = 1228
tilt = 1278

board.digital[Ppan].mode = SERVO
board.digital[Ptilt].mode = SERVO

board.digital[Ptilt].write(tilt)
board.digital[Ppan].write(pan)

pfio.digital_write(0,1)

@app.route("/")
def hello():
  return "You probably want <a href=/static/rover.html> to control the rover. </a>"

########################## end setup ################

@app.route("/light_on")
def light_on():
  pfio.digital_write(0,1)
  return "light on"

@app.route("/light_off")
def light_off():
  pfio.digital_write(0,0)
  return "light off"

def safestop():
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)

####################### pan tilt ####################


@app.route('/o')
def o():
  global pan
  global tilt
  tilt=tilt-50
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ptilt].write(tilt)
  return('%s, %s' % (pan, tilt))


@app.route('/l')
def l():
  global pan
  global tilt
  tilt=tilt+50
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ptilt].write(tilt)
  return('%s, %s' % (pan, tilt))

#  if c==';':
@app.route('/semicolon')
def semicolon():
  global pan
  global tilt
  pan=pan-50
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ppan].write(pan)
  return('%s, %s' % (pan, tilt))


#  if c=='k':
@app.route('/k')
def k():
  global pan
  global tilt
  pan=pan+50
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ppan].write(pan)
  return('%s, %s' % (pan, tilt))


#  if c=='O':
@app.route('/O')
def O():
  global pan
  global tilt
  tilt=tilt-350
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ptilt].write(tilt)
  return('%s, %s' % (pan, tilt))



#  if c=='L':
@app.route('/L')
def L():
  global pan
  global tilt
  tilt=tilt+350
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ptilt].write(tilt)
  return('%s, %s' % (pan, tilt))


#  if c==':':
@app.route('/colon')
def colon():
  global pan
  global tilt
  pan=pan-350
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ppan].write(pan)
  return('%s, %s' % (pan, tilt))


#  if c=='K':
@app.route('/K')
def K():
  global pan
  global tilt
  pan=pan+350
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ppan].write(pan)
  return('%s, %s' % (pan, tilt))

#  resest the camera
@app.route('/resetcamera')
def resetcamera():
  global pan
  global tilt
  pan=1238
  tilt=1238
  board.digital[Ppan].write(pan)
  board.digital[Ptilt].write(tilt)
  return('%s, %s' % (pan, tilt))


############### motor controllers ###################
########################   w    ##########
@app.route("/w")
def w():
  print("w")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(1)
  board.digital[RightForward].write(1)
  Timer(1, safestop).start()
  return("w")

@app.route("/wup")
def wup():
  print("wup")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("wup")
########################   a    ##########
@app.route("/a")
def a():
  print("a")
  board.digital[LeftBack].write(1)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(1)
  Timer(1, safestop).start()
  return("a")

@app.route("/aup")
def aup():
  print("aup")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("aup")
########################   s    ##########
@app.route("/s")
def s():
  print("s")
  board.digital[LeftBack].write(1)
  board.digital[RightBack].write(1)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  Timer(1, safestop).start()
  return("s")

@app.route("/sup")
def sup():
  print("sup")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("sup")
########################   d    ##########
@app.route("/d")
def d():
  print("d")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(1)
  board.digital[LeftForward].write(1)
  board.digital[RightForward].write(0)
  Timer(1, safestop).start()
  return("d")

@app.route("/dup")
def dup():
  print("dup")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("dup")

##################### w a ##################
@app.route("/wa")
def wa():
  print("wa")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(1)
  Timer(1, safestop).start()
  return("wwaaa")

@app.route("/waup")
def waup():
  print("waup")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("wwaaa")

##################### w d ##################
@app.route("/wd")
def wd():
  print("wd")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(1)
  board.digital[RightForward].write(0)
  Timer(1, safestop).start()
  return("wd")

@app.route("/wdup")
def wdup():
  print("wdup")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("wdup")


@app.route("/allstop")
def allstop():
  print("allstop")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("allstop")


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')







