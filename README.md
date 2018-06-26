# comicvine-search

A simple library to interact with the `search` resource of the [ComicVine API](https://comicvine.gamespot.com/api/).

Currently requires **Python 3.6**, as well as the [requests](http://docs.python-requests.org/en/master/) and [requests-cache](https://github.com/reclosedev/requests-cache) packages.


## Usage

The `ComicVineClient` object exposes a single method, `search`.

```python
from comicvine_search.client import ComicVineClient

# You must first register an account in order to obtain an API key.
#   https://comicvine.gamespot.com/api/
cv = ComicVineClient('your-comicvine-api-key')

# Perform a search using the default options.
response = cv.search('transmetropolitan')

# Paginated results are supported using the 'offset' and 'limit' parameters.
response = cv.search('transmetropolitan', limit=5, offset=15)

# Optionally, the type of resources to return in the results can be specified.
response = cv.search('transmetropolitan', resources=['issue', 'volume'])
```

Supported resource types are **character**, **issue**, **location**, **object**, **person**, **publisher**, **story_arc**, **team**, and **volume**.

The `search` function returns a `Response` object containing the JSON results returned by the API. This `Response` object has the following properties accessible:

- status_code **(int)**
- error  **(str)**
- number_of_total_results **(int)**
- number_of_page_results **(int)**
- limit **(int)**
- offset **(int)**
- results **(list[dict])**

```python
>>> response = cv.search('transmetropolitan')
>>> response.status_code
1
>>> response.error
'OK'
>>> response.has_error
False
>>> response.number_of_page_results
10
```

More information can be found in the [API list of resources](https://comicvine.gamespot.com/api/documentation).
