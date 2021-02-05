from board import Board
from person import Mario_here
from calculate import Display
from alarmexception import AlarmException
from config import colors
from getch import _getChUnix as getChar
from check_board import checking_board
import os
import time
import signal
import random


k=1
Test1=Board()
#Test1.getprint()
Test=Mario_here(41,1)
Test2=Display()
def movement():
	def alarmhandler(signum,frame):
		raise AlarmException

	def user_input(timeout=0.1):
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)
		
		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''


				
	char=user_input()

        #Pressing space for shield
	if char=='e':
		quit()

        #For quitting the game
	if char=='q':
		quit()        

        #For moving upside
	if char=='w':
		#first check whether you are standing on surface
		if(Test1.board[Test.x+3][Test.y]==' '):
			#then proceed
			store=Test.x
			s1=Test1.board[Test.x-1][Test.y+2]
			s2=Test1.board[Test.x-1][Test.y+1]
			s3=Test1.board[Test.x-1][Test.y]
			while(Test.x != store-4 and s1 == " " and s2== " " and s3==" "):
				Test.vanish(Test1)
				Test.x-=1
				Test.comeback(Test1)
				s1=Test1.board[Test.x-1][Test.y+2]
				s2=Test1.board[Test.x-1][Test.y+1]
				s3=Test1.board[Test.x-1][Test.y]

	
	#For moving downwards
	if char=='s':
		#simulating gravity
		if(Test1.board[Test.x+3][Test.y]==" " and Test1.board[Test.x+3][Test.y+1]==" " and Test1.board[Test.x+3][Test.y+2]==" "):			
			Test.vanish(Test1)
			print("HElloooo")
			Test.x+=1
			Test.comeback(Test1)



        #For moving rightwards
	if char=='d':
		print("Ateas")
		me=Test.check_coins(Test1, Test,1)
		lets_try=Test.checking_obs(Test1)

		if lets_try==1:
			Test.vanish(Test1)
			Test.y+=1
			Test.comeback(Test1)
		if lets_try==2:
			Test.lives-=1
			
		if me==5:
			for i in range(0,5):
				print("Hiii")
				Test.vanish(Test1)
				'''
				Test1.board[Test.x][Test.y+4+i]=''
				Test1.board[Test.x+2][Test.y+4+i]=''
				Test1.board[Test.x+1][Test.y+4+i]=''
				print(Test1.board[Test.x+1][Test.y+3])
        		'''
        #For moving leftwards
	if char=='a':
		me=Test.check_coins(Test1, Test,0)
		lets_try=Test.checking_obs(Test1)

		if lets_try==1:
			Test.vanish(Test1)
			Test.y-=1
			Test.comeback(Test1)
		if lets_try==2:
			Test.lives-=1			
			#obj_mario.disappear_mario(obj_board)





        #For releasing bullets
	if char=='b':
		quit()


here=time.time()
copy1=here
copy2=here
'''
Test1.getprint(50,0,100)
os.system('clear')
Test1.getprint(50,100,100+100)
'''
os.system('clear')
Test1.getprint(50,0,100)
x=0
while True:
	#os.system("tput reset")
	

	
	Test.timeleft=120- (round(time.time())-round(here))
	print("Time Remaining:--",Test.timeleft,end='\t')
	print("Coins Gained:--",Test.coins,end='\t')
	print("Number of Lives Remaining:--",Test.lives,end='\t')
	print()	
	#Test2.printing_head()

	Test1.creat_coin(23,10)
	Test1.creat_coin(29,40)
	Test.generating(Test1)
	'''
	if(time.time()-copy1 >= 0.05):
		Test1.getprint(50,0+x,100+x)
		x+=3
		'''
		#Test.x+=2
	movement()
	Test1.getprint(50,0+x,100+x)
	#Test.vanish(Test1)
	#Test.comeback(Test1)



	
		
