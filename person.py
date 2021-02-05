import signal
import board
from alarmexception import AlarmException
from check_board import checking_board
from getch import _getChUnix as getChar
from coins import Madhuri
class Mario_here(Madhuri):

	#Madhuri=Board()
	def __init__(self,x,y):
		Madhuri.__init__(self,x,y)
		self.heh=0
		self.coins=0
		self.timeleft=120
		self.red="\u001B[31m"
		self.reset = '\u001b[0m'
		self.yellow = '\u001b[33;1m'
		self.arrows=['>','>','>','>','>','>','>']
		self.indexx=0
		self.shot=0
		self.drag=['<','<','<','<','<','<','<','<','<']
		self.uj=[0,0,0,0,0,0,0,0,0]
		self.vj=[0,0,0,0,0,0,0,0,0]
		self.xj=[0,0,0,0,0,0,0]
		self.yj=[0,0,0,0,0,0,0]
		self.lives=5
		self.x=x
		self.y=y
		self.give=[" ","$"]
		self.head = '{^__^}'
		self.neck='[PP]'
		self.body='E'
		self.bottom='[ON]'
		self.legs='// //'
		self.move_forward='\\ \\'
		self.drlives=5
		self.move_up='|| ||'
		self.magenta = '\u001b[35;1m'
		self.__array = [['{','^','}'],[' ','O',' '],['/' , ' ' , '/']]

	def shoot(self,Test1,d1,d2):
		Test1.board[d1][d2-4]=self.red+self.drag[self.shot]+self.reset
		self.uj[self.shot]=d1
		self.vj[self.shot]=d2-4
		self.shot+=1

	def mission(self,Test1,m,d1,d2):
		for i in range(m):
			Test1.board[self.uj[i]][self.vj[i]-4]=Test1.board[self.uj[i]][self.vj[i]]		
			Test1.board[self.uj[i]][self.vj[i]]=" "
			self.vj[i]-=4


	def call_me(self,Test1):
		Test1.board[self.x+1][self.y+4]=self.magenta+self.arrows[self.indexx]+self.reset
		self.xj[self.indexx]=self.x+1
		self.yj[self.indexx]=self.y+4
		self.indexx+=1
	def bullets(self,Test1,m):
		for i in range(m):
			try:
				if(i+3 <=900 and Test1.board[self.xj[i]][self.yj[i]]==self.red+"@"+self.reset or Test1.board[self.xj[i]][self.yj[i]+1]==self.red+"@"+self.reset or Test1.board[self.xj[i]][self.yj[i]+2]==self.red+"@"+self.reset or Test1.board[self.xj[i]+1][self.yj[i]+1]==self.red+"@"+self.reset or Test1.board[self.xj[i]+1][self.yj[i]+2]==self.red+"@"+self.reset):
					Test1.board[self.xj[i]][self.yj[i]]="@"
					Test1.board[self.xj[i]][self.yj[i]+1]=="@"
					Test1.board[self.xj[i]][self.yj[i]+2]=="@"
					Test1.board[self.xj[i]+1][self.yj[i]+2]=="@"
					self.coins+=1
				else:
					if(i+5<=900 and self.yj[i]+4 <= 900):
						Test1.board[self.xj[i]][self.yj[i]+4]=Test1.board[self.xj[i]][self.yj[i]]
						Test1.board[self.xj[i]][self.yj[i]]=" "
					self.yj[i]+=4
			except:
				continue
		for i in range(m):
			try:
				if self.yj[i]>=840:
					Test1.board[self.xj[i]][self.yj[i]]=" "
					self.drlives-=1
					self.coins+=5
				if self.vj[i]<=self.y or self.vj[i]<=self.y-1 or self.vj[i]<=self.y+1 :
					Test1.board[self.uj[i]][self.vj[i]]=" "
					self.lives-=1
			except:
				continue



	def check_coins(self,Test1,Test,c):
		#c=1 is checking rightwards
		print("Ayee")
		if(c==1):
			#print(Test.x,Test.y)
			#print(Test.y+3)
			if(Test1.board[Test.x+1][Test.y+3]==Test1.yellow+"$"+Test1.reset):
				print("Hehe")
				#Test1.board[Test.x+1][Test.y+4]=="@"
				self.coins+=5
				return 5
			elif(Test1.board[Test.x][Test.y+3]==Test1.yellow+"$"+Test1.reset): 
				print("Hehe")
				#Test1.board[Test.x][Test.y+4]=="@"
				self.coins+=5
				return 5
			elif(Test1.board[Test.x+2][Test.y+3]==Test1.yellow+"$"+Test1.reset):
				#Test1.board[Test.x+2][Test.y+4]=="@"
				print("Hehe")
				self.coins+=5
				return 5




		#c=0 is checking leftwards
		if(c==0):
			if(Test1.board[Test.x+1][Test.y+3]==Test1.yellow+"$"+Test1.reset or Test1.board[Test.x][Test.y+3]==Test1.yellow+"$"+Test1.reset or Test1.board[Test.x+2][Test.y+3]==Test1.yellow+"$"+Test1.reset):
				self.coins+=5
				return 5
		

	def generating(self,Test1):
		for i in range(42,45,1):
			for j in range(1,4):
				Test1.board[i][j]=self.__array[i-42][j-1]
	

	def generat(self,Test1):
		for i in range(42,45,1):
			for j in range(2,5):
				if j==2:
					Test1.board[i][j-1]=='-'
				elif j==5:
					Test1.board[i][j+1]=='-'
				Test1.board[i][j]=self.__array[i-42][j-1]
		
	def vanish(self,grid):
		for i in range(self.x,self.x+3):
			for j in range(self.y,self.y+3):
				grid.board[i][j]=" "
				if grid.board[i][j+1]==self.yellow+"$"+self.reset:
					self.coins+=1
					grid.board[i][j+1]=" "

	def comeback(self,Test1):
		for i in range(self.x,self.x+3):
			for j in range(self.y,self.y+3):
				if Test1.board[i][j+1]==self.yellow+"$"+self.reset:
					self.coins+=1
				Test1.board[i][j]=self.__array[i-self.x][j-self.y]


	def checking_obs(self,Test1):
		if (Test1.board[self.x+1][self.y+3] in self.give
			and Test1.board[self.x+1][self.y+3] in self.give
			and Test1.board[self.x+2][self.y+3] in self.give):

			return 1
		
		#elif (self.x+3<=46 and self.y<=1196 and Test1.board[self.x + 1][self.y + 3] == "@" or Test1.board[self.x+2][self.y+3] == "@"):
		#    return 2
		
		else:
			return 3
	
	def mags(self,h1,h2,grid,magss):
		#Magnet coordination
		if magss ==1 :
			for i in range(20):
				self.heh=1
				if(self.x-i==h1 or self.x-2-i==h1):
					self.vanish(grid)
					self.x=h1-1
					print("!@#$%^&*")
					self.comeback(grid)
				elif(self.y+i==h2):
					self.vanish(grid)
					self.y=h2-1
					self.x=h1-1
					self.comeback(grid)
	#	return magss






		
		