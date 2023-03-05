# pyminmax
``minmax()`` function
```
minmax(iterable, *, key=None)
minmax(iterable, *, default, key=None)
minmax(arg1, arg2, *args, key=None)
```
With a single iterable argument, return its smallest and largest items as a
tuple pair. The *default* keyword-only argument specifies an object to return if
the provided iterable is empty. If the iterable is empty and *default* is not
provided, a *ValueError* is raised.

With two or more arguments, return the smallest and largest argument as a
tuple pair.

The *key* argument specifies a one-argument ordering function like that used
for ``list.sort()``.

If multiple items are minimal or maximal, the function returns the first ones
encountered.

It is written in C, adapted straight from CPython's [implementation](https://github.com/python/cpython/blob/a74cd3ba5de1aad1a1e1ee57328b54c22be47f77/Python/bltinmodule.c#L1728)
of ``min()``, ``max()``.
## Installation
```
pip install pyminmax
```
## Usage
```python3
>>> from pyminmax import minmax
>>> minmax([5, 2, 0, 100, -100, 10])
(-100, 100)
>>> minmax((), default=1)
1
```
## Test
Once installed, run the test suite via
```
python -m unittest pyminmax.tests --verbose
```
