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
            xml_dict = self._xml_to_dict(xml_data)
            data = xml_dict['AIRPORT_STATUS_INFORMATION']
        else:
            data = xml_data
        return data

    def _cycle_delays(self, list_name, key_name):
        """
        Internal method to cycle through current delays and stops, and
        return information about specific ones.
        """
        data = self.delays()
        for delay in data['Delay_type']:
            if list_name in delay:
                return delay[list_name][key_name]

    def ground_delays(self):
        """Returns a list of airports currently experiencing ground delays."""
        return self._cycle_delays('Ground_Delay_List', 'Ground_Delay')

    def ground_stops(self):
        """Returns a list of airports currently experiencing ground stops."""
        return self._cycle_delays('Ground_Stop_List', 'Program')

    def delay_list(self):
        """
        Returns a list of all airports experiencing arrival or departure
        delays.
        """
        return self._cycle_delays('Arrival_Departure_Delay_List', 'Delay')
