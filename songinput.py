def song_input (x):
	b=1
	while b < 21 :
		print(b,' ',x)
		b+=1
	
def song_game():
	a=1
	while a < 11:
		song = input('What is your favorite song?')
		song_input(song)
		a+=1
song_game()
