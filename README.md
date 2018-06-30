# comicvine-search

[![Build Status](https://travis-ci.org/jessebraham/comicvine-search.svg?branch=master)](https://travis-ci.org/jessebraham/comicvine-search) [![Coverage Status](https://coveralls.io/repos/github/jessebraham/comicvine-search/badge.svg?branch=master)](https://coveralls.io/github/jessebraham/comicvine-search?branch=master)

A simple client library to interact with the `search` resource of the [ComicVine API](https://comicvine.gamespot.com/api/).

**Note:** ComicVine requires you [register an account](https://comicvine.gamespot.com/api/) in order to obtain an API key. Queries will *not* be successful if a valid API key is not provided.


## Requirements

Currently requires **Python 3.6**. It is recommended you use [pyenv](https://github.com/pyenv/pyenv) and [pipenv](https://github.com/pypa/pipenv).  

Additionally, the [requests](https://github.com/requests/requests) and [requests-cache](https://github.com/reclosedev/requests-cache) packages are required. Caching is used because the API is limited to 200 requests per resource, per hour.

```bash
# Install the appropriate version of Python3 using Pyenv
$ pyenv install 3.6.5
# Activate the virtual environement
$ pipenv shell
# Install all dependencies
(comicvine-search-gvTaHBnv)$ pipenv install
```


## Usage

The `ComicVineClient` object exposes a single method, `search`. The `search` method takes the following parameters:

| Name          | Description                                                        | Default  |
|:--------------|:-------------------------------------------------------------------|:---------|
| **query**     | The search term to query the API with.                             |          |
| **offset**    | The starting offset of the search results; used for pagination.    | **0**    |
| **limit**     | The maximum number of results to return to the client. **MAX 10**. | **10**   |
| **resources** | A list of resource types to include in the search results.         | **None** |
| **use_cache** | Specify whether or not the use the requests cache.                 | **True** |

Supported resource types are **character**, **issue**, **location**, **object**, **person**, **publisher**, **story_arc**, **team**, and **volume**.


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


### Response

The `search` function returns a `Response` object containing the results returned by the API. The `Response` object has the following properties accessible:

| Property                | Type |
|:------------------------|:-----|
| status_code             | **int** |
| error                   | **str**
| number_of_total_results | **int**
| number_of_page_results  | **int**
| limit                   | **int**
| offset                  | **int**
| results                 | **list[dict]**
| has_error               | **bool**

```python
>>> response = cv.search('the astounding wolfman')
>>> response.status_code
1
>>> response.error
'OK'
>>> response.has_error
False
>>> response.number_of_total_results
39
>>> response.number_of_page_results
10
>>> len(response.results)
10
```

More information on the API can be found in the [API list of resources](https://comicvine.gamespot.com/api/documentation).


## To Do

### Short-Term

- [x] ~~Add a suite of tests and configure TravisCI, Coveralls~~
- [ ] Improve unit testing and mocking
- [ ] Better documentation

### Long-Term

- [ ] Create a `setup.py` file
- [ ] Better handling of rate limiting by the API
- [ ] Marshal results into their respective objects, by resource type
- [ ] Figure out some sort of fuzzy search/matching, if possible
