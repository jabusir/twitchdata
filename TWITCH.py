import requests 
url = 'https://api.twitch.tv/helix/games/top?first=10'
headers = {'Client-ID': 'td952w1le1li3hlpngfmmd13sxk7ls'} 

r = requests.get(url, headers=headers) #Fetches the data from Twitch's API 

interData = r.json() 

listofGame = []
for i, d in enumerate(interData['data']): #Creates a list of the games numbering them from 0-9 
	print(str(i) + ' ' + d['name'])
	listofGame.append((d['name'], d['id'])) 

choice = int(input("Choose a game: ")) 

print(listofGame[choice][0]) 

id = listofGame[choice][1] 

r2 = requests.get('https://api.twitch.tv/helix/streams?first=10&game_id={id}'.format(id = id), headers = headers) #Fetches the user id's of the top 10 streams from Twtich's API

interName = r2.json() 

listofUserId = []

for i in interName['data']:
	listofUserId.append(i['user_id']) 

r3url = "https://api.twitch.tv/helix/users?" 
for i in listofUserId: 
	r3url+='id={id}&'.format(id = i)

r3url = r3url.strip('&') 

r3 = requests.get(r3url, headers = headers) #Takes the streamers user ID's and turns them in to their respective display names

idData = r3.json() 

namesViews = []

for i in idData['data']: #Appends all the streamers with their respective view counts to a list of tuples
	namesViews.append((i['display_name'],i['view_count']))
	
for i in namesViews: #Prints final list of names with respective views line by line 
	print([i],"\n") 