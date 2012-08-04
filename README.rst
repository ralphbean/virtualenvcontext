virtualenvcontext
=================

:Author: Ralph Bean <ralph.bean@gmail.com>

.. comment: split here

Example
-------

>>> from virtualenvcontext import VirtualenvContext

>>> try:
>>>     import kitchen
>>> except ImportError as e:
>>>     print "kitchen is definitely not installed in system-python"

>>> with VirtaulenvContext("my-venv"):
>>>     import kitchen
>>>     print "But it *is* installed in my virtualenv"

>>> try:
>>>     import kitchen
>>> except ImportError as e:
>>>     print "But once I exit that block, I lose my powers again..."

Caveat:
-------
It expects that you're using
`virtualenvwrapper <http://pypi.python.org/pypi/virtualenvwrapper>`_ but
you should be anyways.

Get this project:
-----------------
Source:  http://github.com/ralphbean/virtualenvcontext/

pypi:    http://pypi.python.org/pypi/virtualenvcontext/


