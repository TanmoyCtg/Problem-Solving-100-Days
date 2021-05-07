import time, threading

print('Start of program.')

def takeANap():

	time.sleep(5)
	print('Wake up!')

takeANap()
print('End of program')

