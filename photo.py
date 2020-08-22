#!/usr/bin/python3
import os
import time
photo_name = "hello.jpg"
os.system("raspistill -o "+photo_name)
time.sleep(10)
photo_name = "motto.jpg"
os.system("raspistill -o "+photo_name)
