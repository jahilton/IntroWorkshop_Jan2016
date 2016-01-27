from datetime import date
from datetime import datetime

def main():
	today = date.today()
	print('Today is:',today)
	print('Date components',today.day,today.month,today.year)
	today = datetime.now()
	print('Current time:',today)
	t = datetime.time(datetime.now())
	print('time:',t)
	wd = date.weekday(today)
	print(wd)
main()
