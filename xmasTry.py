#!/usr/bin/python3.8
from datetime import *
date_format = "%m/%d/"
now = datetime.now()
xmas = datetime(now.year, 12, 25)
delta = xmas - now
final= delta.days
if final > 0:
 print(final, "days until Christmas!")
elif final == 0:
 print("Merry Christmas!")
elif final < 0:
 print("It is past Christmas, wait until next year!")