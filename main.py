import os
import eel

from Backend.feachers import *

eel.init("Frontend")
os.system('start msedge.exe --app=http://127.0.0.1:5501/Frontend/index.html')

playAssistantSound
eel.start("index.html", mode="none", host="localhost", block=True)
