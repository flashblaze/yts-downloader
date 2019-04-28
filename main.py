import requests

r = requests.get('https://yts.am/api/v2/list_movies.json?limit=2')
r_dict = r.json()
movieURL = r_dict['data']['movies'][0]['torrents'][0]['url']
movieTitle = r_dict['data']['movies'][0]['title']
with open(movieTitle + '.torrent', 'wb') as f:
    f.write(requests.get(movieURL).content)
