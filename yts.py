import requests
from bs4 import BeautifulSoup
import argparse
from requests.exceptions import Timeout


def main():
    """
    Parsing the 2nd argument which is the movie title
    For example:
        python main.py 'The Trip To Spain'

    In the above case, arg[1],  which is 'The Trip To Spain', will be stored in name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('movie', type=str,
                        help='Movie name')
    args = parser.parse_args()
    name = args.movie

    try:
        r = requests.get('https://yts.am/browse-movies', timeout=15)
    except Timeout:
        print('Request timeout')
    else:

        soup = BeautifulSoup(r.text, 'lxml')
        h2 = soup.find_all('h2')
        movie_count = int((str(h2)[5:11].replace(',', '')))
        titles = []
        ids = []
        page = 1

        while True and page < movie_count / 50:

            # Parameters to be added at the end of the url
            payload = {
                'limit': 50,
                'page': page
            }
            r = requests.get(
                'https://yts.am/api/v2/list_movies.json', params=payload)
            print("Searching on page: " + str(page))

            if(r.status_code != 200):
                print('Unable to get data\nExiting!')
                exit()

            # Using json method, since the response is in json
            r_dict = r.json()

            for i in range(payload['limit']):
                titles.append(r_dict['data']['movies'][i]['title'])
                ids.append(r_dict['data']['movies'][i]['id'])

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
                finalTitle = titles[val]
                finalId = ids[val]
                payload = {
                    'movie_id': finalId
                }

                r = requests.get(
                    'https://yts.am/api/v2/movie_details.json', params=payload)
                r_new_dict = r.json()
                print("\n")

                print("Choose your option:")
                for url in r_new_dict['data']['movie']['torrents']:
                    print("Quality: " + url['quality'] + "\t" +
                          "Size: " + url['size'] + "\t" + "Type: " + url['type'])

                choice = int(input())
                with open(finalTitle.replace(':', '') + '.torrent', 'wb') as f:
                    f.write(requests.get(
                        r_new_dict['data']['movie']['torrents'][choice - 1]['url']).content)
                exit()

            page += 1
            payload['page'] = page
            r_dict.clear()
            del titles[:]
            del ids[:]
