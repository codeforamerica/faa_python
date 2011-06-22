FAA Python
==========

A Python wrapper for the Federal Aviation Administration's API.


Usage
-----


```python
>>> from faa import FAA

>>> # Find all current delays in the US.
... FAA().delays()

>>> # Search for the status of a specific airport.
... FAA().status('SFO')

```

Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
