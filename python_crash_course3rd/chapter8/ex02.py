from itertools import tee
def	city_country(city, country):
	res = str(f"{city}, " + country)
	return (res)

def	make_album(artist_name, album_title, n_musics=None):
	res = dict()
	res = {
		"Artist Name": artist_name,
		"Album name": album_title
	}
	if n_musics:
		res["Number of songs"] = int(n_musics)
	return (res)


city = 'natal'
country = 'brasil'

result = city_country(city.title(), country.title())
print(result)

album = make_album('jorge ben jor'.title(), 'capadocia'.title())
album2 = make_album('Racionais MCs', 'Sobrevivendo ao inferno'.title())
album3 = make_album('Pearl Jam', 'Alive', 12)
print(album, album2, album3, sep='\n')

print("Please insert a artist name and album to create a dict")
flag = True
while flag:
	artist_name = input("Enter artist name: ")
	album_name = input("Enter album name: ")
	n_songs = int(input("Enter the number of songs(0 for default): "))

	res = make_album(artist_name, album_name, n_songs)
	print(res)
	text = input("Want to insert another album? (y/n)")
	if (text == 'n'):
		flag = False
