#DISCLAIMER: this program is developed for educational purposes only
#developed following tutorial by Naster Code Online at https://www.youtube.com/watch?v=jDRhsqi7jOg

#simple program that opens web pages in the default browser. 

import webbrowser
import time
import random



while True:
	sites= random.choice(['google.com', 'youtube.com', 'yahoo.com','facebook.com', 'instagram.com', 'gmail.com'])	#site to be rendered in new browser tab
	visit="http://{}".format(sites)	#make site into valid url
	webbrowser.open(visit)	#open valid url in web browser
	
	#open next tab after time period of 5-20 seconds
	seconds=random.randrange(5,20)	
	time.sleep(seconds)
	############
