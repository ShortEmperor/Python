#!/usr/bin/python3.8
import datetime

class xmastree:
	def __init__(self,size,trunk):
		self.size=size
		self.trunk=trunk
	def showtree(self):
		for i in range(0,self.size):
			 print((self.size-i)*" ",i*" *")
		for i in range(0,self.trunk):
			 print (self.size*" ","*")
 
atree=xmastree(15,3)




def Main():
    days_left = str(datetime.datetime(2020, 12, 24) - datetime.datetime.now()).split()

    if days_left[0] == '0:00:00':
        print('Merry Xmas!')
        atree.showtree()
    else:
        print('There\'s {0} days left until Xmas :)'.format(days_left[0]))

if __name__ == '__main__':
    Main()