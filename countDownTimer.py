#Countdown timer
# adapted from: https://www.youtube.com/watch?v=8d2cWG5J4lc

import time
import subprocess

#work and break times in seconds
workTime  = 55 * 60
breakTime = 15 * 60

def countdown(duration, message):
	#try-except allows to use keyboard interrupts (Cntl-C) to pause and resume
	#second try-except is the resume, and uses recursion to re-implement with 
	#only the remaining time.  Here, we're using KeyboardInterrupt.. Im not sure
	# what SystemExit does...
    try:
    	for elapsedSeconds in range(0, duration):
			remainingTime    = duration - elapsedSeconds
			remainingMinutes = remainingTime / 60
			remainingSeconds = remainingTime % 60
			print  message, remainingMinutes , ':' , remainingSeconds
			time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
    	print " \n Timer paused. To resume, press Cntl-C, (" , str(remainingMinutes), ":", str(remainingSeconds) , " remaining)"
        try:
        	time.sleep(1000)
        except (KeyboardInterrupt, SystemExit):
        	print " \n resuming..."
        	time.sleep(1)
        	countdown(remainingTime - 1, message)
 
print "\n \nWell hello there!  Get ready to work!  \n\n  To pause,  type Cntl-C."
print "  To resume, type Cntl-C again\n"
countdown(workTime, 'Continue Working for')
	
print '\n Take a break! \n'
subprocess.call(["play", "singingBowl4s.wav"])

countdown(breakTime, 'Continue not working for')
	
print '\n Done! \n'
subprocess.call(["play", "singingBowl4s.wav"])
