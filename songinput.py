def song_input (x):
	b=1
	while b < 21 :
		print(b,' ',x)
		b+=1
	
def song_game():
	a=1
	songlist = []
	while a < 11:
		song = input('What is your favorite song?')
		songlist.append(song)
		a+=1
	x=0	
	while x < 10:	
		song_input(songlist[x])
		x+=1

song_game()
