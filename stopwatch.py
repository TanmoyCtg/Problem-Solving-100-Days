import time

print('Press Enter to begin, Afterwards, press enter to "click" the stopwatch press ctrl-c')

input()

print('started')

startTime = time.time()
lastTime = startTime
lapNum=1

try:
	while True:
		input()
		laptime = round(time.time()-lastTime,2)
		totaltime = round(time.time()-startTime, 2)
		print("Lap #%s: %s (%s) "%(lapNum, totaltime, laptime), end='')
		lapNum +=1
		lastTime = time.time()
except KeyboardInterrupt:
	print('\nDone')