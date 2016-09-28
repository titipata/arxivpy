# Arxivpy

Python wrapper for [arXiv API](http://arxiv.org/help/api/index).
Here are related libraries and repositories: [arxiv.py](https://github.com/lukasschwab/arxiv.py),
[.py](https://arxiv.org/help/api/examples/python_arXiv_parsing_example.txt)
[arXiv](http://arxiv.org/) is an open-access journal which has 1M+ e-prints in
Physics, Mathematics, Computer Science, Quantitative Biology,
Quantitative Finance and Statistics.

## Example

Here is an example on how to use `arxivpy`.

```python
import arxivpy
articles = arxivpy.query(start_index=0, max_index=200,
                         fields=['cs.CV', 'cs.LG', 'cs.CL', 'cs.NE', 'stat.ML'],
                         wait_time=5.0, sort_by='lastUpdatedDate') # grab 200 articles
```

This will give list of dictionary parsed from arXiv XML file.
More fields available can be seen from [wiki page](https://github.com/titipata/arxivpy/wiki).
Moreover, we can download articles to local directory as follows

```python
arxivpy.download(articles, path='arxiv_pdf')
```

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
