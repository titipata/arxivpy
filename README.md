# Arxiv Parser [WIP]

Python wrapper for [arXiv API](http://arxiv.org/help/api/index). Here is an
example on how to use.

```python
import arxivpy
articles = arxivpy.query(start_index=0, max_index=200,
                         fields=['cs.CV', 'cs.LG', 'cs.CL', 'cs.NE', 'stat.ML'],
                         wait_time=5.0, sort_by='lastUpdatedDate') # grab 200 articles
```

This will give list of dictionary from arXiv. We can also download articles
to local directory

```python
arxivpy.download(articles, path='arxiv_pdf')
```

## Dependencies

- [feedparser](https://github.com/kurtmckee/feedparser)
