#program that deletes typed input as soon as it is typed. 

from pynput.keyboard import Key, Controller, Listener

keyboard=Controller()

def press(key):
	if (key==Key.backspace):	#do nothing if key is backspace (otherwise would be stuck in some form of forever loop)
		pass
	else:
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
	

	
		
def on_release(key):
	if key==Key.esc:	#break out of loop if escape key is pressed (provides means of stopping the program, otherwise restart would be necessary)
		return False

	
with Listener(on_press=press, on_release=on_release) as listener:
	listener.join()
	
