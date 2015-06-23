class song :
	"""Song Class"""
	
	def __init__(self,title,length) :
		self.name = title
		self.time = length
		self.songInfo = "Title: " + self.name + " Length: " + self.time

		
def song_input (x):
	b=1
	while b < 21 :
		print(b,' ',x)
		b+=1
	
def song_game():
	a=0
	songlist = []
	while a < 10:
		songtitle = input('What is your favorite song?')
		songtime = input('How long is that song?')
		song_entry = song(songtitle,songtime)
		songlist.append(song_entry.songInfo)
		a+=1
	x=0	
	while x < 10:	
		song_input(songlist[x])
		x+=1

song_game()