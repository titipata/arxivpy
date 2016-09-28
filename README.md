# Arxivpy

Python wrapper for [arXiv API](http://arxiv.org/help/api/index).
Here are related libraries and repositories: [arxiv.py](https://github.com/lukasschwab/arxiv.py),
[python_arXiv_parsing_example.py](https://arxiv.org/help/api/examples/python_arXiv_parsing_example.txt)
and [arxiv-sanity-preserver](https://github.com/karpathy/arxiv-sanity-preserver).
[arXiv](http://arxiv.org/) is an open-access journal which has 1M+ e-prints in
Physics, Mathematics, Computer Science, Quantitative Biology,
Quantitative Finance and Statistics.

## Example

Here is an example on how to use `arxivpy`.

```python
import arxivpy
articles = arxivpy.query(search_query=['cs.CV', 'cs.LG', 'cs.CL', 'cs.NE', 'stat.ML'],
                         start_index=0, max_index=200,
                         wait_time=5.0, sort_by='lastUpdatedDate') # grab 200 articles
```

This will give list of dictionary parsed from arXiv XML file.
You can use other search queries, for example:

```python
search_query=['cs.DB', 'cs.IR']
search_query='cs.DB' # select only Databases papers
search_query='au:kording' # author name includes Kording
search_query='ti:deep+AND+ti:learning' # title with `deep` and `learning`
```

More search query prefixes, boonlean and categories available can be seen
from [wiki page](https://github.com/titipata/arxivpy/wiki).
Other functionality is that we can download articles to local directory.
Here is snippet to download articles.

```python
arxivpy.download(articles, path='arxiv_pdf')
```

**Note from API**

- the maximum number of results returned from a single call (`max_index`)
is limited to 30000 in slices of at most 2000 at a time.
- In cases where the API needs to be called multiple times in a row,
we encourage you to play nice and incorporate a 3 second delay in your code.

## Installation

First, you need to install [feedparser](https://github.com/kurtmckee/feedparser) library.
Then, clone the repository and run `setup.py` to install the package.

```bash
git clone https://github.com/titipata/arxivpy
cd arxivpy
python setup.py install
```

## Dependencies

- [feedparser](https://github.com/kurtmckee/feedparser)
