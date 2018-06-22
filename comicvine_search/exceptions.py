#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Contains all custom exception definitions used by the ComicVine API client.
These exceptions are thrown only when HTTP errors occur, more specifically
when the status code in the response is not **200**.

ComicVine API Information & Documentation:
https://comicvine.gamespot.com/api/
https://comicvine.gamespot.com/api/documentation
'''


class ComicVineApiError(Exception):
    '''
    A generic exception raised by the ComicVine API client when no more
    suitable exception type exists.
    '''
    pass


class ComicVineUnauthorizedError(Exception):
    '''
    An exception raised when an unauthorized request has been made to the
    ComicVine API. This usually occurs when the API key is not provided or is
    otherwise invalid.
    '''
    pass


class ComicVineForbiddenError(Exception):
    '''
    An exception raised when a forbidden request has been made to the
    ComicVine API. This usually occurs when the User-Agent header was not
    provided with the request.
    '''
    pass
