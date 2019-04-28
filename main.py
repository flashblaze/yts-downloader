import requests
import sys

# Parameters to be added at the end of the url
params = {
    'limit': 20,
    'page': 1
}
r = requests.get('https://yts.am/api/v2/list_movies.json', data=params)

# Using json method, since the response is in json
r_dict = r.json()
urls = []
titles = []

for i in range(params['limit']):
    urls.append(r_dict['data']['movies'][i]['torrents'][0]['url'])
    titles.append(r_dict['data']['movies'][i]['title'])

"""
Parsing the 2nd argument which is the movie title
For example:
    python main.py 'The Trip To Spain'

In the above case, arg[1],  which is 'The Trip To Spain', will be stored in name
"""
name = sys.argv[1].lower()

print(titles)
count = 0
val = 0
flag = 0
for title in titles:
    if name in title.lower():
        print('Title is available!')
        val = count
        flag = 1
    else:
        count += 1

if(flag == 0):
    print("Title not found. Try again!")
else:
    finalURL = urls[val]
    finalTitle = titles[val]

    # movieTitle = r_dict['data']['movies'][0]['title']
    with open(finalTitle + '.torrent', 'wb') as f:
        f.write(requests.get(finalURL).content)
