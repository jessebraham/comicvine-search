#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
ComicVine API Information & Documentation:
https://comicvine.gamespot.com/api/
https://comicvine.gamespot.com/api/documentation
'''

import datetime


class Response(object):
    '''
    Documented status code/error message combinations:
      1:   OK
      100: Invalid API Key
      101: Object Not Found
      102: Error in URL Format
      103: 'jsonp' format requires a 'json_callback' argument
      104: Filter Error
    '''

    def __init__(self, json):
        '''
        Store each key-value pair from the JSON response in class variables
        named after the key. Be sure to provide the proper types for the
        default values.

        :param json: The JSON response returned by the API request.
        :type  json: dict
        '''

        self.status_code = json.get('status_code', 0)
        self.error = json.get('error', '')
        self.number_of_total_results = json.get('number_of_total_results', 0)
        self.number_of_page_results = json.get('number_of_page_results', 0)
        self.limit = json.get('limit', 0)
        self.offset = json.get('offset', 0)
        self.results = json.get('results', 0)
        self.timestamp = datetime.datetime.utcnow()

    @property
    def has_error(self):
        # 1: "OK" is the only status code that indicates success. If any other
        # status code is returned, an error of some sort is present.
        return self.status_code != 1

    def __repr__(self):
        return f'<comicvine_search.response.Response(' \
               f'status_code={self.status_code!r}) ' \
               f'object at {hex(id(self))}>'
