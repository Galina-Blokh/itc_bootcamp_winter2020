import grequests
from bs4 import BeautifulSoup
from collections import OrderedDict
import logging
import timeit

# log-file will be created in the same dir
logging.basicConfig(filename='grequests_logging.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
LINK = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
LINK_PATTERN = '/title/tt'
BATCHES = 10


def grequests_top_250_directors_links(link):
    '''get the link from which one you have to collect a list of movie links
    :returns list of links'''

    x = []
    rs = grequests.get(link)
    response = grequests.map([rs], size=BATCHES)
    for i, res in enumerate(response):
        soup = BeautifulSoup(res.content, 'html.parser')
        x = [str(LINK[:20] + l.get('href')) for l in soup.find_all('a') if str(l.get('href')).startswith(LINK_PATTERN)]
    return list(dict.fromkeys(x))


def clean_movie(text):
    ''' gets text from movie request :returns the pure name of the movie'''

    clean_movie_name = str(text.strip().split("\n")[0][:-7].strip())
    return clean_movie_name


def get_num_director_movie_name(list_of_links):
    '''gets list of links for top 250 movies
    :returns list of directors names'''

    dict_titles = {}
    rs = (grequests.get(movie) for movie in list_of_links)
    responses = grequests.imap(rs, size=BATCHES)
    logging.info('!!!---The director and movie_name download is starting---!!!')
    for res in responses:
        content = res.content
        soup = BeautifulSoup(content, 'html.parser')
        try:
            movie = clean_movie(soup.find('h1', class_='').text)
            logging.info("movie_name '{}' is cached successfully".format(movie))
        except:
            logging.exception('The class name in movies link is absent')
            movie = clean_movie(soup.find('div', class_="title_wrapper").text)
        name = soup.find('div', class_="credit_summary_item").text.split(':\n')[1].split('|')[0]
        actor = soup.find('div', class_="plot_summary").text
        if actor.__contains__('Jack Nicholson'):
            logging.warning("Jack Nicholson is acted in the '{}' movie".format(movie))

        dict_titles[list_of_links.index(res.request.url) + 1] = '- ' + str(movie) + ' - ' + str(name)
        # shows the % of downloading to not be boring
        print('Downloading ...{}%'.format(round(len(dict_titles) / len(list_of_links) * 100, 2)))
    sorted_dict = OrderedDict(sorted(dict_titles.items(), key=lambda t: t[0]))
    return sorted_dict


def main():
    '''prints the result of program'''

    pages_urls = grequests_top_250_directors_links(LINK)
    answer = get_num_director_movie_name(pages_urls)
    for k, v in answer.items():
        print(k, v)


if __name__ == '__main__':
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    execution_time = stop - start
    logging.info("Program Executed in {} min \n\n".format(round(execution_time / 60), 2))  # It returns time in min
