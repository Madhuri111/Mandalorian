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
#allow_active=1
abc=0
powerup=0
up=0
a=[1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]
g=0

def shld():
		Test1.board[Test.x][Test.y-1]="-"
		Test1.board[Test.x+1][Test.y-1]="-"
		Test1.board[Test.x+2][Test.y-1]="-"
		Test1.board[Test.x][Test.y+1]="-"
		Test1.board[Test.x+1][Test.y+1]="-"
		Test1.board[Test.x+2][Test.y+1]="-"
		make_active()
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

		#Pressing firing the bullets
	if char=='b':
		Test.call_me(Test1)
	#For quitting the game
	if char=='q':
		quit()

	#For activating the shield
	if char=='l':
		#if allow_active==1:
		madhuri=1
	#For moving upside
	if char=='w':
		up=time.time()
		g=0
		#first check whether you are standing on surface
		for i in range(Test.x,Test.x+3):
			for j in range(Test.y,Test.y+3):
				if(Test1.yellow+"$"+Test1.reset==Test1.board[i][j+1]):
					Test.coins+=1
				#Test1.board[i][j+1]=" "
		if(Test.x-1>0 and Test1.board[Test.x-1][Test.y]==' ' or Test1.board[Test.x+3][Test.y]=='-'):
			#then proceed
			store=Test.x
			s1=Test1.board[Test.x-1][Test.y+2]
			s2=Test1.board[Test.x-1][Test.y+1]
			s3=Test1.board[Test.x-1][Test.y]
			while(Test.x != store-4 and s1 == " " and s2== " " and s3==" " or s1 == Test.yellow+"$"+Test.reset or s2 == Test.yellow+"$"+Test.reset or s3==Test.yellow+"$"+Test.reset):
				if(Test1.board[Test.x-1][Test.y]!=Test1.blue+'#'+Test1.reset):
					Test.vanish(Test1)
					if powerup==1:
						Test.x-=3
					else:
						Test.x-=1					
					Test.comeback(Test1)
					s1=Test1.board[Test.x-1][Test.y+2]
					s2=Test1.board[Test.x-1][Test.y+1]
					s3=Test1.board[Test.x-1][Test.y]


		lets_try=Test.checking_obs(Test1)
		#if(Test1.board[Test.x+3][Test.y]==" " and Test1.board[Test.x+3][Test.y+1]==" " and Test1.board[Test.x+3][Test.y+2]==" "):			
		if lets_try==1:
			Test.vanish(Test1)
			if Test.x-1 <=1:
				Test.x-=1
			Test.comeback(Test1)
	#For moving downwards
	if char=='s':
		for i in range(Test.x,Test.x+3):
			for j in range(Test.y,Test.y+3):
				if(Test1.yellow+"$"+Test1.reset==Test1.board[i][j+1]):
					Test.coins+=1
				Test1.board[i][j+1]=" "
		#simulating gravity
		lets_try=Test.checking_obs(Test1)
		#if(Test1.board[Test.x+3][Test.y]==" " and Test1.board[Test.x+3][Test.y+1]==" " and Test1.board[Test.x+3][Test.y+2]==" "):			
		if lets_try==1 and Test1.board[Test.x+1][Test.y]==Test1.green+"-"+Test1.reset or Test1.board[Test.x+1][Test.y]==Test1.green+"~"+Test1.reset or Test1.board[Test.x+1][Test.y]==Test1.green+"#"+Test1.reset  :
			Test.vanish(Test1)
			print("HElloooo")
			if powerup==1:
				Test.x+=3
			else:
				Test.x+=1
			Test.comeback(Test1)



		#For moving rightwards
	if char=='d':
		#me=Test.check_coins(Test1, Test,1)
		lets_try=Test.checking_obs(Test1)

		#if(Test1.board[Test.x][Test.y+4]=="$"):
		#	print("I can do this")
		for i in range(Test.x,Test.x+3):
			for j in range(Test.y,Test.y+3):
				if(Test1.yellow+"$"+Test1.reset==Test1.board[i][j+1]):
					Test.coins+=1
				Test1.board[i][j+1]=" "
		if lets_try==1 and Test.y < x+95:
			Test.vanish(Test1)
			if powerup==1:
				Test.y+=3
			else:
				Test.y+=1
			Test.comeback(Test1)
		if lets_try==2:
			Test.lives-=1
		'''	
		if me==5:
			for i in range(0,5):
				print("Hiii")
				Test.vanish(Test1)
				
				Test1.board[Test.x][Test.y+4+i]=''
				Test1.board[Test.x+2][Test.y+4+i]=''
				Test1.board[Test.x+1][Test.y+4+i]=''
				print(Test1.board[Test.x+1][Test.y+3])
				'''
		#For moving leftwards
	if char=='a':
		#me=Test.check_coins(Test1, Test,0)
		lets_try=Test.checking_obs(Test1)

		if lets_try==1 and Test.y > x:
			print("HEre"+str(Test.y)+"  "+str(x))
			Test.vanish(Test1)
			if powerup==1:
				print("powera")
				Test.y-=3
			else:
				Test.y-=1			
			Test.comeback(Test1)
		if lets_try==2:
			Test.lives-=1			
			#obj_mario.disappear_mario(obj_board)







here=time.time()
copy1=here
copy2=here
madhuri=0

'''
Test1.getprint(50,0,100)
os.system('clear')
Test1.getprint(50,100,100+100)
'''
x=0
me=0
magss=0
Test1.tunnel(Test1.board, 30)
#Test1.cloud(Test1.board,2,50)
Test1.fire(Test1.board)
#h1=random.randint(9,11)
#h2=random.randint(100,200)
h1=8
h2=120
hehe=0
Test1.enemy(Test1.board,20,850)
d1=20
d2=800
Test1.board[h1][h2]=str(h1)+str(h2)
magss=1
jj=1
tested=0
Test1.board[30][300]="P"
is_come=1

	
while True:
	#os.system("tput reset")
	#os.system('clear')


	Test1.getprint(50,0+x,100+x,Test)
	Test.generating(Test1)
	movement()

	#Test1.enemy(Test1.board,20,850)
	if(Test1.board[Test.x][Test.y+3]=="P" or Test1.board[Test.x+1][Test.y+3]=="P" or Test1.board[Test.x+2][Test.y+3]=="P" or Test1.board[Test.x+3][Test.y+3]=="P" or Test1.board[Test.x+3][Test.y+2]=="P"):
		powerup=1

	if(Test1.board[Test.x+3][Test.y]==" " # simulate gravity
		and Test1.board[Test.x+3][Test.y+1]==" "
		and Test1.board[Test.x+3][Test.y+2]==" " or Test1.board[Test.x+3][Test.y]==Test.yellow+"$"+Test.reset or Test1.board[Test.x+3][Test.y+1]==Test.yellow+"$"+Test.reset or Test1.board[Test.x+3][Test.y+2]==Test.yellow+"$"+Test.reset):
		if(Test1.board[Test.x+3][Test.y]==Test.yellow+"$"+Test.reset or Test1.board[Test.x+3][Test.y+1]==Test.yellow+"$"+Test.reset or Test1.board[Test.x+3][Test.y+2]==Test.yellow+"$"+Test.reset):
			Test.coins+=1
		Test.vanish(Test1)
		Test.x+=1
		Test.comeback(Test1)
	
	#Decreasing lives for fire beams
	if madhuri==0:
		if(Test1.board[Test.x][Test.y]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+1][Test.y+1]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+2][Test.y+1]==Test1.red+"@"+Test1.reset or Test1.board[Test.x][Test.y-1]==Test1.red+"@"+Test1.reset or Test1.board[Test.x][Test.y-2]==Test1.red+"@"+Test1.reset):
			Test.lives-=1
			print("Plzz")
		if(Test1.board[Test.x+1][Test.y+2]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+1][Test.y]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+3][Test.y]==Test1.red+"@"+Test1.reset):
			Test.lives-=1
			print("Plzz")
		if(Test1.board[Test.x-1][Test.y+1]==Test1.red+"@"+Test1.reset or Test1.board[Test.x-1][Test.y]==Test1.red+"@"+Test1.reset or Test1.board[Test.x-1][Test.y+2]==Test1.red+"@"+Test1.reset):
			Test.lives-=1
			print("Plzz")
		if(Test1.board[Test.x][Test.y+3]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+3][Test.y+2]==Test1.red+"@"+Test1.reset):
			Test.lives-=1
			print("Plzz")
		if(Test1.board[Test.x+1][Test.y+3]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+1][Test.y-1]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+2][Test.y-1]==Test1.red+"@"+Test1.reset):
			Test.lives-=1
		if(Test1.board[Test.x+3][Test.y+1]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+3][Test.y+2]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+1][Test.y+3]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+3][Test.y+3]==Test1.red+"@"+Test1.reset):
			Test.lives-=1
		if(Test1.board[Test.x-1][Test.y-1]==Test1.red+"@"+Test1.reset or Test1.board[Test.x-1][Test.y+2]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+2][Test.y+3]==Test1.red+"@"+Test1.reset or Test1.board[Test.x+1][Test.y+3]==Test1.red+"@"+Test1.reset):
			Test.lives-=1

	elif madhuri==1:
		#Test.generat(Test1)
		print("Shield is active ")
		'''
		Test1.board[Test.x][Test.y-1]="-"
		Test1.board[Test.x+1][Test.y-1]="-"
		Test1.board[Test.x+2][Test.y-1]="-"
		Test1.board[Test.x][Test.y+1]="-"
		Test1.board[Test.x+1][Test.y+1]="-"
		Test1.board[Test.x+2][Test.y+1]="-"
		'''


	'''
	if(Test1.board[Test.x+3][Test.y]=="$" or Test1.board[Test.x+3][Test.y+1]=="$" or Test1.board[Test.x+3][Test.y+2]=="$"):
		Test.x+=3
		Test.vanish(Test1)
		Test1.board[Test.x+3][Test.y]==" "
		Test1.board[Test.x+3][Test.y+1]==" "
		Test1.board[Test.x+3][Test.y+2]==" "
		Test.coins+=1
		print("MEME")
	#Test1.getprint(50,0+x,100+x)
	'''
	Test.bullets(Test1,Test.indexx)
	
	Test.mags(h1,h2,Test1,magss)
	if (h2 < x ):
		magss=0
	''''
	if(d2-100 < x):
		print("DRAGON HERE")
	Test.shoot(Test1,d1,d2)
		movement()
	'''
	if(x>600):
		Test.shoot(Test1,d1,d2)
		Test.mission(Test1,Test.shot,d1,d2)
	if(abs(time.time()-copy1) >= 0.02):
		if(x<800):
			Test1.getprint(50,0+x,100+x,Test)
			copy1=time.time()
			x+=2
			Test.vanish(Test1)
			Test.y+=2
			Test.comeback(Test1)
	

	
	Test.timeleft=120- ((time.time())-(here))
	print("Time Remaining:--",round(Test.timeleft),end='\t' + str(x))
	print("power is "+str(powerup))
	print("Coins Gained:--",Test.coins,"Hello " ,end='\t')
	print("Number of Lives :--",Test.lives,end='\t' )
	print()

	if(Test.lives<= -100 or Test.timeleft<=0 ):
		print("Your time is Over,Good bye and your score is ",Test.coins)
		#os.system("killall")
		quit()
	if(Test.drlives <= 0):
		print("Your time is Over,Good bye and your score is ",Test.coins)
		quit()


	
'''
	In main functin , move funcion for bullets make it +=3 and increase it's coordinates by 3
	bullet one list, x coordinates one list, y coordinates one list 
	printing bullets +=2 row column of mario
'''