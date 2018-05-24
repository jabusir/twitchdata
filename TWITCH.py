import requests 
url = 'https://api.twitch.tv/helix/games/top?first=10'
headers = {'Client-ID': 'td952w1le1li3hlpngfmmd13sxk7ls'} 

r = requests.get(url, headers=headers)

interData = r.json() 

listofGame = []
for i, d in enumerate(interData['data']):
	print(str(i) + ' ' + d['name'])
	listofGame.append((d['name'], d['id'])) 

choice = int(input("Choose a game: "))

print(listofGame[choice][0]) 

id = listofGame[choice][1] 

r2 = requests.get('https://api.twitch.tv/helix/streams?first=10&game_id={id}'.format(id = id), headers = headers)

interName = r2.json() 

listofUserId = []

for i in interName['data']:
	listofUserId.append(i['user_id']) 

r3url = "https://api.twitch.tv/helix/users?"
for i in listofUserId: 
	r3url+='id={id}&'.format(id = i)

r3url = r3url.strip('&') 

r3 = requests.get(r3url, headers = headers) 

idData = r3.json() 

namesViews = []

for i in idData['data']:
	namesViews.append((i['display_name'],i['view_count']))
	
print(namesViews)