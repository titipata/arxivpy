# Arxiv Parser [WIP]

Python wrapper for Arxiv API

```
import arxivpy
articles = arxivpy.fetch_arxiv(start_index=0, max_index=200,
                               fields=['cs.CV', 'cs.LG', 'cs.CL', 'cs.NE', 'stat.ML'],
                               wait_time=5.0, sort_by='lastUpdatedDate') # grab 200 articles
```

## Dependencies

- [feedparser](https://github.com/kurtmckee/feedparser)
