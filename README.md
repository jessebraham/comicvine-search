# comicvine-search

A simple library to interact with the `search` resource of the [ComicVine API](https://comicvine.gamespot.com/api/).

Currently requires **Python 3.6**, as well as the [requests](http://docs.python-requests.org/en/master/) and [requests-cache](https://github.com/reclosedev/requests-cache) packages.


## Usage

```python
from comicvine_search.client import ComicVineClient

# You must first register an account in order to obtain an API key.
#   https://comicvine.gamespot.com/api/
cv = ComicVineClient('your-comicvine-api-key')

# Perform a search using the default options.
results = cv.search('transmetropolitan')

# Paginated results are supported using the 'offset' and 'limit' parameters.
results = cv.search('transmetropolitan', limit=5, offset=15)

# Optionally, the type of resources to return in the results can be specified.
results = cv.search('transmetropolitan', resources=['issue', 'volume'])
```

The `search` function returns a `Response` object containing the JSON results returned by the API. This `Response` object has the following properties accessible:

- status_code
- error
- number_of_total_results
- number_of_page_results
- limit
- offset
- results

More information can be found in the [API list of resources](https://comicvine.gamespot.com/api/documentation).


## To Do

- [ ] Create a `Response` object and parse results into it; return this rather than JSON.
- [ ] Convert `Client` class methods to "private" methods where appropriate.
