from datetime import datetime


# Quick and rough gps calculator (fra)
gps_begin = datetime(1980, 1, 6, 0, 0, 0) # Don't change this; it is the beginning of the gps time count

year = int(raw_input('Year: '))
month = int(raw_input('Month: '))
day = int(raw_input('Day: '))
hour = int(raw_input('Hour: '))
minute = int(raw_input('Minute: '))
second = int(raw_input('Second: '))
##### The day and time we want to analyse
the_day = datetime(year, month, day, hour , minute, second) # 10th of August 2017, 00:26:22

leap_seconds = 18 # as of Dec 2016
gps = int((the_day - gps_begin).total_seconds()) + leap_seconds
print 'GPS time: ' + str(gps)
