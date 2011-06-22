FAA Python
==========

A Python wrapper for the Federal Aviation Administration's API.


Usage
-----


```python
>>> from faa import FAA

>>> # Find all current delays in the US.
... FAA().delays()
{'lots': {'and': {'lots': 'of delay data'}}}

>>> # Search for the status of a specific airport.
... FAA().status('SFO')
{'data': {'specific to': 'SFO'}}

>>> # Get back a list of all ground delays.
... FAA().ground_delays()
[{'ground': 'delay'}, {'ground': 'delay'}, ...]

>>> # Get back a list of all ground stops.
... FAA().ground_stops()
[{'ground': 'stop'}, {'ground': 'stop'}, ...]

>>> # Get back a list of all arrival and depature delays.
... FAA().delay_list()
[{'arrival': 'delay'}, {'departure': 'delay'}, ...]
```

Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
