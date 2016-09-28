import os
import sys
import time
import urllib
import feedparser
import random
from dateutil import parser

if sys.version_info[0] == 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve

def query(start_index=0,
          max_index=100,
          results_per_iteration=100,
          wait_time=5.0,
          fields=['cs.CV', 'cs.LG', 'cs.CL', 'cs.NE', 'stat.ML'],
          sort_by='lastUpdatedDate',
          sort_order=None):
    """
    Function to parse Arxiv XML using the API.

    Parameters
    ==========

    start_index: int, start index

    max_index: int, end or max index

    results_per_iteration: number of article parsing per iteration
        this control so we don't parse too many articles at once

    wait_time: float, waiting time when scrape more than

    fields: list or str, list of fields
        see the end of this page http://arxiv.org/help/api/user-manual#python_simple_example
        for more fields see https://github.com/titipata/arxivpy/wiki
        if no field specified, use 'all' as default

    sort_by: str, either "relevance" or "lastUpdatedDate" or "submittedDate" or None
    sort_order: str, either "ascending" or "descending" or None
    """

    base_url = 'http://export.arxiv.org/api/query?'

    if isinstance(fields, str) or len(fields) == 1:
        search_query = 'cat:%s' % fields
    elif isinstance(fields, list) or len(fields) > 1:
        search_query = '+OR+'.join(['cat:%s'%f for f in fields])
    elif not search_query:
        search_query = 'all'
    else:
        search_query = 'all'
    search_query = 'search_query=%s' % search_query

    if results_per_iteration is None:
        results_per_iteration = end_index

    if sort_by is not None:
        sort_by_query = 'sortBy=%s' % sort_by
    else:
        sort_by_query = ''

    if sort_order is not None:
        sort_order_query = 'sortOrder=%s' % sort_order
    else:
        sort_order_query = ''

    articles_all = list()
    for i in range(start_index, max_index, results_per_iteration):
        start_query = 'start=%i' % int(start_index)
        max_results_query = 'max_results=%i' % int(start_index + results_per_iteration)

        ql = [search_query, sort_by_query, sort_order_query, start_query, max_results_query]
        query_list = [q for q in ql if q is not '']
        query = '&'.join(query_list)

        articles = list()
        response = urllib.request.urlopen(base_url + query).read()
        entries = feedparser.parse(response)
        if len(entries['entries']) == 0:
            print('Check query %s from the website if it returns anything' % (base_url + query) )
        else:
            for entry in entries['entries']:
                term = entry['arxiv_primary_category']['term']
                main_author = entry['author']
                authors = ', '.join([author['name'].strip() for author in entry['authors']])
                link = entry['link']
                for e in entry['links']:
                    if 'title' in e:
                        if e['title'] == 'pdf':
                            pdf_link = e['href']
                    else:
                        pdf_link = 'http://arxiv.org/pdf/%s' % link.split('/')[-1]
                title = entry['title_detail']['value'].replace('\n', ' ').strip()
                abstract = entry['summary'].replace('\n', ' ')
                publish_date = parser.parse(entry['published'])
                article = {'id': entry['link'].split('/')[-1],
                           'term': term,
                           'main_author': main_author,
                           'authors': authors,
                           'link': link,
                           'pdf_link': pdf_link,
                           'title': title,
                           'abstract': abstract,
                           'publish_date': publish_date}
                articles.append(article)
            if i > start_index: time.sleep(wait_time + random.uniform(0, 3))
            articles_all.extend(articles)
    return articles_all

def download(articles, path='arxiv_pdf'):
    """
    Give list of parsed Arxiv dictionary, download
    """
    if not os.path.isdir(path):
        os.mkdir(path)
    for article in articles:
        if article['pdf_link']:
            filename = article['id'] + '.pdf'
            urlretrieve(article['pdf_link'], os.path.join(path, filename))
        else:
            print("No pdf available for arXiv at %d" % article['pdf_link'])
