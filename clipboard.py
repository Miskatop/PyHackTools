# Simple Clipboad Hacking
from pyperclip import paste

def function(*args, **kwargs):...

def on_change(callback=function, fun=paste):
	old = ''
	while True:
		try:
			new = fun()
			if new != old:
				old = new
				callback(new)
		except Exception as e:
			print(f'[ ERROR ] - {e}.')
		except KeyboardInterrupt:
			break
