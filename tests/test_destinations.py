#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import systranGeographicApi
import systranGeographicApi.configuration

class DestinationsApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        systranGeographicApi.configuration.load_api_key(api_key_file)
        self.api_client = systranGeographicApi.ApiClient()
        self.destinations_api = systranGeographicApi.DestinationsApi(self.api_client)

    def test_geographic_destinations_list_get(self):
        result = self.destinations_api.geographic_destinations_list_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_destinations_get_get(self):
        id = "56600a3a14c46414e0275cf0"
        print 'Use a valid "id" and uncomment below codes to test'
        # result = self.destinations_api.geographic_destinations_get_get(id=id)
        # self.assertIsNotNone(result)
        # print result.__repr__()

if __name__ == '__main__':
    unittest.main()

