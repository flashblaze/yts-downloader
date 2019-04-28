import requests

params = {
    'limit': 20,
    'page': 1
}

r = requests.get('https://yts.am/api/v2/list_movies.json', data=params)
r_dict = r.json()
urls = []
titles = []
for i in range(params['limit']):
    urls.append(r_dict['data']['movies'][i]['torrents'][0]['url'])
    titles.append(r_dict['data']['movies'][i]['title'])

name = 'the trip to spain'.lower()

print(titles)
count = 0
val = 0
for title in titles:
    if name in title.lower():
        print('yes')
        val = count
    else:
        count += 1

finalURL = urls[val]
finalTitle = titles[val]

# movieTitle = r_dict['data']['movies'][0]['title']
print(finalTitle)
with open(finalTitle + '.torrent', 'wb') as f:
    f.write(requests.get(finalURL).content)
