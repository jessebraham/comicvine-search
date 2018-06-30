#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import pytest
import responses

from comicvine_search import ComicVineClient
from comicvine_search.exceptions import (
    ComicVineForbiddenError, ComicVineUnauthorizedError
)


class TestComicVineClient(object):

    @pytest.fixture
    def client(self):
        # Set an environment variable prior to running your tests containing
        # your ComicVine API key. A file named `.env` in the root project
        # directory will be loaded automatically when Pipenv activates.
        #   export COMICVINE_API_KEY="your-comicvine-api-key"
        api_key = os.environ.get('COMICVINE_API_KEY')
        return ComicVineClient(api_key)

    # Client Tests

    @responses.activate
    def test_comic_vine_client_raises_unauthorized(self):
        responses.add(responses.GET, 'https://www.comicvine.com/api/search/',
                      json={}, status=401)

        cv = ComicVineClient('')

        with pytest.raises(ComicVineUnauthorizedError):
            cv.search('runaways')

    @responses.activate
    def test_comic_vine_client_raises_forbidden(self, client):
        responses.add(responses.GET, 'https://www.comicvine.com/api/search/',
                      json={}, status=403)
        client.HEADERS = None

        with pytest.raises(ComicVineForbiddenError):
            client.search('the boys')

    def test_comic_vine_client(self, client):
        # TODO: don't test directly against api
        response = client.search('transmetropolitan')

        assert response is not None
        assert response.number_of_total_results > 0
        assert len(response.results) > 0

    def test_comic_vine_client_search_limit(self, client):
        # TODO: don't test directly against api
        limit = 5

        response = client.search('watchmen', limit=limit)

        assert response.number_of_page_results == limit
        assert len(response.results) == limit

    def test_comic_vine_client_with_resources(self, client):
        # TODO: don't test directly against api
        resources = ['issue', 'volume']

        response = client.search('saga', resources=resources)

        for result in response.results:
            assert result['resource_type'] in resources

    # Response Tests

    @responses.activate
    def test_comicvine_search_response_has_no_error(self, client):
        responses.add(responses.GET, 'https://www.comicvine.com/api/search/',
                      json={'status_code': 1, 'error': 'OK'}, status=200)

        response = client.search('outcast')

        assert response.status_code == 1
        assert response.error == 'OK'
        assert response.has_error is False

    @responses.activate
    def test_comicvine_search_response_has_error(self, client):
        responses.add(responses.GET, 'https://www.comicvine.com/api/search/',
                      json={'status_code': 101, 'error': 'Object Not Found'},
                      status=200)

        response = client.search('')

        assert response.status_code == 101
        assert response.error == 'Object Not Found'
        assert response.has_error is True

    @responses.activate
    def test_comicvine_search_response_repr(self, client):
        responses.add(responses.GET, 'https://www.comicvine.com/api/search/',
                      json={}, status=200)

        response = client.search('y the last man')

        resp = str(response)
        assert resp.startswith('<comicvine_search.response.Response(')
        assert str(response.status_code) in resp
