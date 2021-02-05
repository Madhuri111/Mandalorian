import config
import random

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 
class Board():
	
	def __init__(self):
		self.bl=950
		self.bh=50
		self.board=[[' ' for i in range(self.bl)] for j in range(self.bh)] 
		self.rows=[]
		self.__tunnel=[]
		self.__tun=[]
		self.__fire1=[]
		self.__fire2=[]
		self.__fire3=[]
		self.__dragon=[]
		self.green = '\u001b[32;1m'
		self.__magnet=[]
		self.red="\u001B[31m"
		self.reset = '\u001b[0m'
		self.blue = '\u001b[34;1m'
		self.magenta = '\u001b[35;1m'
		self.cyan = '\u001b[36;1m'
		self.yellow = '\u001b[33;1m'
		self.white = '\u001b[37;1m'
		self.bgblue= "\u001B[44m"
		self.obstacles=[]

		for i in range(self.bl):
			self.board[self.bh-5][i]=self.green+"-"+self.reset
			self.board[self.bh-4][i]=self.green+"-"+self.reset
			self.board[self.bh-3][i]=self.green+"#"+self.reset
			self.board[self.bh-2][i]=self.green+"~"+self.reset
			self.board[self.bh-1][i]=self.green+"#"+self.reset
			self.board[0][i]=self.blue+"#"+self.reset
			#self.board[1][i]="#"

	def getprint(self,xa,ya,yb,Test):
		print("\033[0;0H",end="")
		for i in range(20):
			Test.arrows.append('>')
			Test.xj.append(0)
			Test.yj.append(0)
			Test.drag.append('<')
			Test.uj.append(0)
			Test.vj.append(0)
		for x in range(0,xa):
			for y in range(ya,yb):
				print(self.board[x][y],end='')
			print(" ")

	def creat_cloud(self,x,y):
		#for i in range(0,5):
		self.board[x][y+9]=self.cyan+"@"+self.reset
		self.board[x+1][y+8]=self.cyan+'@'+self.reset
		self.board[x+1][y+10]=self.cyan+'@'+self.reset
		self.board[x+1][y+4]=self.blue+'('+self.reset
		self.board[x+1][y+15]=self.blue+')'+self.reset
		self.board[x+2][y+2]=self.blue+'('+self.reset
		self.board[x+2][y+17]=self.blue+')'+self.reset
		self.board[x+2][y+7]=self.cyan+'@'+self.reset
		self.board[x+2][y+11]=self.cyan+'@'+self.reset
		self.board[x+3][y]=self.blue+'('+self.reset
		self.board[x+3][y+6]=self.cyan+'@'+self.reset
		self.board[x+3][y+9]=self.cyan+'@'+self.reset
		self.board[x+3][y+13]=self.cyan+'@'+self.reset
		self.board[x+3][y+19]=self.blue+')'+self.reset
		self.board[x+4][y-2]=self.blue+'('+self.reset
		self.board[x+4][y+21]=self.blue+')'+self.reset
	
	
	def creat_mountain(self,top,y,gap):
		y=y-1
		for i in range(top,top+5):
			self.board[i][y]=self.green+'/'+self.reset
			self.board[i][y+gap]=self.green+"\\"+self.reset
			y=y-1
			gap=gap+2

	def creat_coin(self,x,y):
		self.board[x][y]="$"
		self.board[x][y+1]="$"
		self.board[x][y+2]="$"
		self.board[x][y+3]="$"
		self.board[x][y+4]="$"
		'''
		self.board[x][y]=+$
		self.board[x][y+1]=+$
		self.board[x][y+2]=+$
		self.board[x][y+3]=+$
		self.board[x][y+4]=+$
		'''

	def creat_brick(self,x,y):
		self.board[y-1][x-1]=self.magenta+" ##BRICK_BRICK###"+self.reset
		self.board[y][x]=self.magenta+'[@*@'+self.reset
		self.board[y][x+1]=self.magenta+'$~$]'+self.reset
		self.board[y][x+2]=self.magenta+'[@*@'+self.reset
		self.board[y][x+3]=self.magenta+'$~$]'+self.reset
		self.board[y+1][x]=self.magenta+'[&*&'+self.reset
		self.board[y+1][x+1]=self.magenta+'(*)]'+self.reset
		self.board[y+1][x+2]=self.magenta+'[&*&'+self.reset
		self.board[y+1][x+3]=self.magenta+'(*)]'+self.reset
		
	def creat_waterfall(self,x,y):
		self.board[y][x] = '|'
		self.board[y + 1][x] = '|'
		self.board[y][x + 1] =  '_'
		self.board[y][x + 2] =  '_'
		self.board[y][x + 3] =  '_'
		self.board[y][x + 4] =  '_'
		self.board[y][x + 5] =  '_'
		self.board[y][x + 6] =  '_'
		self.board[y][x + 7] =  '_'
		self.board[y][x + 8] =  '_'
		self.board[y][x + 9] =  '|'
		self.board[y + 1][x + 9] =  '|'

	def tunnel(self,grid,d):
		with open("coin.txt") as obj:
			for line in obj:
				self.__tunnel.append(line.strip('\n'))
		c=random.randint(10,35)
		while(d<900):
			e=d
			f=c
			for i in range(4):
				for j in range(10):
					grid[c][d] = self.yellow+self.__tunnel[i][j]+self.reset
					d+=1
				d=e
				c+=1
			c=f
			d+=random.randint(25,40) 

	def magnet(self,grid,c,d):
		with open("magnet.txt") as obj:
			for line in obj:
				self.__magnet.append(line.strip('\n'))
		grid[c][d]="MM"


	def cloud(self,grid,c,d):
		with open("cloud.txt") as obj:
			for line in obj:
				self.__tun.append(line.strip('\n'))

		while(d<900):
			e=d
			f=c
			for i in range(len(self.__tun)):
				for j in range(len(self.__tun[0])):
					grid[c][d] = self.__tun[i][j]
					d+=1
				d=e
				c+=1
			c=f
			d+=random.randint(30,40) 

	def enemy(self,grid,c,d):
		
		with open("dragon.txt") as obj:
			for line in obj:
				self.__dragon.append(line.strip('\n'))
		for i in range(len(self.__dragon)):
			for j in range(len(self.__dragon[i])):
				grid[c+i][d+j] = self.cyan+self.__dragon[i][j]+self.reset
				
	def enemy_disappear(self,grid,c,d):
		s1=d
		s2=c
		for i in range(len(self.__dragon)):
			for j in range(len(self.__dragon[i])):
				grid[c][d] = " "
				d+=1
			d=s1
			c+=1
		c=s2
	def fire(self,grid):
		with open("a1.txt") as obj:
			for line in obj:
				self.__fire1.append(line.strip('\n'))
		with open("a2.txt") as obj:
			for line in obj:
				self.__fire2.append(line.strip('\n'))
		with open("a3.txt") as obj:
			for line in obj:
				self.__fire3.append(line.strip('\n'))
		c=random.randint(11,20)
		d=random.randint(50,100)
		while(d<700):
			e=d
			f=c
			for i in range(len(self.__fire1)):
				for j in range(len(self.__fire1[0])):
					grid[c][d] = self.red+self.__fire1[i][j]+self.reset
					d+=1
				d=e
				c+=1
			c=random.randint(5,30)
			d+=random.randint(100,700)
		c=random.randint(15,25)
		d=random.randint(50,150)
		while(d<700):
			e=d
			f=c
			for i in range(len(self.__fire2)):
				for j in range(len(self.__fire2[0])):
					grid[c][d] = self.red+self.__fire2[i][j]+self.reset
					d+=1
				d=e
				c+=1
			c=random.randint(5,30)
			d+=random.randint(100,150)
		c=random.randint(20,30)
		d=random.randint(100,250)
		
		while(d<800):
			e=d
			f=c
			for i in range(len(self.__fire3)):
				for j in range(len(self.__fire3[i])):
					grid[c][d] = self.red+self.__fire3[i][j]+self.reset
					d+=1
				d=e
				c+=1
			c=random.randint(10,15)
			d+=random.randint(100,150)
		
		




active=0