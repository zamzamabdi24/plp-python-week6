# Week 6 Assignment

`safe_tools.py` contains safe functions for division, number conversion, and dictionary field lookup.

`unbreakable.py` asks for a whole number and handles invalid input without crashing.

The `if` check cannot catch `abc` on its own because Python raises a `ValueError` while trying to convert `abc` to an integer with `int()`. A `try` and `except` block is needed to catch that error.
