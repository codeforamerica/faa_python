#!/usr/bin/env python

"""Unit tests for the Python wrapper for the FAA API."""

import unittest

from mock import Mock

from faa.api import api
from faa import faa, FAA

from test_delays_data import DELAYS


class TestDelaysMethod(unittest.TestCase):

    def setUp(self):
        api.xml2dict = Mock(return_value=DELAYS)
        faa.urlopen = Mock()

    def test_default_delays_method(self):
        FAA().delays()
        expected_url = 'http://www.fly.faa.gov/flyfaa/xmlAirportStatus.jsp'
        faa.urlopen.assert_called_with(expected_url)
        self.assertTrue(api.xml2dict.called)

    def test_delays_method_can_return_xml_data(self):
        FAA().delays(output_format=None)
        self.assertFalse(api.xml2dict.called)


class TestStatusMethod(unittest.TestCase):

    def setUp(self):
        api.urlopen = Mock()
        api.json = Mock()
        api.xml2dict = Mock()

    def test_status_method_for_DFW(self):
        FAA().status('DFW')
        expected_url = 'http://services.faa.gov/airport/status/DFW?format=json'
        api.urlopen.assert_called_with(expected_url)
        self.assertTrue(api.json.loads.called)

    def test_status_method_with_lowercase_airport(self):
        FAA().status('sfo')
        expected_url = 'http://services.faa.gov/airport/status/SFO?format=json'
        api.urlopen.assert_called_with(expected_url)
        self.assertTrue(api.json.loads.called)

    def test_status_method_can_return_json(self):
        FAA().status('JFK', output_format=None)
        self.assertFalse(api.json.loads.called)

    def test_status_method_can_return_xml_format(self):
        FAA().status('PDX', format='xml')
        expected_url = 'http://services.faa.gov/airport/status/PDX?format=xml'
        api.urlopen.assert_called_with(expected_url)
        self.assertFalse(api.xml2dict.called)


if __name__ == '__main__':
    unittest.main()
