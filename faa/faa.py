#!/usr/bin/env python

"""Python wrapper for the Federal Aviation Administration's API."""

from api import API, urlopen


class FAA(API):
    """Python wrapper for the Federal Aviation Administration's API."""

    def __init__(self):
        super(FAA, self).__init__()
        self.base_url = 'http://services.faa.gov/airport/status'

    def status(self, airport, **kwargs):
        """Find the status information for a specific airport."""
        if 'format' not in kwargs:
            kwargs['format'] = 'json'
            if 'output_format' not in kwargs:
                kwargs['output_format'] = 'json'
        airport = airport.upper()
        self.call_api(airport, **kwargs)

    def delays(self, output_format='xml'):
        """
        Return status information for all US airports currently
        encountering delays.
        """
        status_url = 'http://www.fly.faa.gov/flyfaa/xmlAirportStatus.jsp'
        xml_data = urlopen(status_url).read()
        if output_format:
            data = self._xml_to_dict(xml_data)
        else:
            data = xml_data
        return data
