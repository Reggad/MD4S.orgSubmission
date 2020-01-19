#!/usr/bin/env python3
#!/usr/bin/env python2


import datetime
import sys
import re

print("Number of arguments '" + str(len(sys.argv))+"'")
print("Argument list:" + str(sys.argv))

inputdate = ""
regexdate = re.compile('[0-9]*-[0-9]*-[0-9]*')
regextime = re.compile('[0-9]*:[0-9]*')

if(len(sys.argv) > 2):
	if regexdate.match(sys.argv[1]) is not None and regextime.match(sys.argv[2]) is not None:
		date = sys.argv[1].split("-")
		time = sys.argv[2].split(":")
		try:
			inputdate = datetime.datetime(day=int(date[0]) ,month=int(date[1]), year=int(date[2]), hour=int(time[0]),minute=int(time[1]))
		except:
			print("Please ensure you have supplied a valid date and time")
			exit()
	else:
		print("Your input did not match the expected format. Please ensure the date you passed is dd/mm/yyyy and the time argument is hh:mm")
		exit()
else:
	inputdate = datetime.datetime.now()

drawtime = datetime.time(21, 30)

if((inputdate.weekday() == 1) or (inputdate.weekday() == 6) and inputdate.time() < drawtime):
	inputdate = inputdate.replace(hour=21, minute=30, second=00) 
	print("Next lottery draw takes place today at 21:30 (" + str(inputdate))
else:
	inputdate = inputdate +datetime.timedelta(days=1)
	while((inputdate.strftime("%A") != 'Tuesday') and (inputdate.strftime("%A") != 'Sunday')):
		inputdate = inputdate +datetime.timedelta(days=1)
		print("current day is '" + inputdate.strftime("%A") +"'")
	inputdate = inputdate.replace(hour=21, minute=30, second=00)
	print("Next lottery draw takes place at " +str(inputdate))