# comicvine-search

A simple library to interact with the `search` resource of the [ComicVine API](https://comicvine.gamespot.com/api/).


## Requirements

Currently requires **Python 3.6**. It is recommended you use [pyenv](https://github.com/pyenv/pyenv) and [pipenv](https://github.com/pypa/pipenv).  

Additionally, the [requests](https://github.com/requests/requests) and [requests-cache](https://github.com/reclosedev/requests-cache) packages are required. Caching is used because the API is limited to 200 requests per resource, per hour.

```bash
$ pyenv install 3.6.5
$ pipenv shell
(comicvine-search-gvTaHBnv)$ pipenv install
```


## Usage

The `ComicVineClient` object exposes a single method, `search`.


### Example

```python
from comicvine_search import ComicVineClient

# You must first register an account in order to obtain an API key.
#   https://comicvine.gamespot.com/api/
cv = ComicVineClient('your-comicvine-api-key')

# Perform a search using the default options.
response = cv.search('transmetropolitan')

# Paginated results are supported using the 'offset' and 'limit' parameters.
response = cv.search('brian k vaughan', limit=2, offset=4)

# Optionally, the type of resources to return in the results can be specified.
response = cv.search('kill or be killed', resources=['issue', 'volume'])
```

Supported resource types are **character**, **issue**, **location**, **object**, **person**, **publisher**, **story_arc**, **team**, and **volume**.


### Response

The `search` function returns a `Response` object containing the results returned by the API. The `Response` object has the following properties accessible:

- status_code **(int)**
- error  **(str)**
- number_of_total_results **(int)**
- number_of_page_results **(int)**
- limit **(int)**
- offset **(int)**
- results **(list[dict])**
- has_error **(bool)**

```python
>>> response = cv.search('the astounding wolfman')
>>> response.status_code
1
>>> response.error
'OK'
>>> response.has_error
False
>>> response.number_of_page_results
10
>>> len(response.results)
10
```

More information on the API can be found in the [API list of resources](https://comicvine.gamespot.com/api/documentation).
