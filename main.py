import requests
import sys


"""
Parsing the 2nd argument which is the movie title
For example:
    python main.py 'The Trip To Spain'

In the above case, arg[1],  which is 'The Trip To Spain', will be stored in name
"""
name = sys.argv[1].lower()

urls = []
titles = []
page = 1

while True and page < 500:

    # Parameters to be added at the end of the url
    payload = {
        'limit': 50,
        'page': page
    }
    r = requests.get('https://yts.am/api/v2/list_movies.json', params=payload)
    print(r.url)
    # Using json method, since the response is in json
    r_dict = r.json()

    for i in range(payload['limit']):
        urls.append(r_dict['data']['movies'][i]['torrents'][0]['url'])
        titles.append(r_dict['data']['movies'][i]['title'])

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
        pass
    else:
        finalURL = urls[val]
        finalTitle = titles[val].replace(':', '')
        with open(finalTitle + '.torrent', 'wb') as f:
            f.write(requests.get(finalURL).content)
        exit()

    page += 1
    payload['page'] = page
    r_dict.clear()
