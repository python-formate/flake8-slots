========
Usage
========

This library provides the Flake8 plugin ``flake8-slots``  to require __slots__ to be defined for subclasses of immutable types.


Flake8 codes
--------------

.. flake8-codes:: flake8_slots

	SLOT000
	SLOT001
	SLOT002

For subclasses of immutable types it is recommended to use ``__slots__ = ()`` to keep the memory usage down.
For subclasses of :class:`str` it is possible to define other variables which may be set on instances. For example:

.. code-block:: python

	class MyString(str):

		__slots__ = ("a_variable", )

which will allow a value to be assigned to ``a_variable``.

Pre-commit hook
----------------

``flake8-encodings`` can also be used as a ``pre-commit`` hook
See `pre-commit <https://github.com/pre-commit/pre-commit>`_ for instructions

Sample ``.pre-commit-config.yaml``:

.. pre-commit:flake8:: 0.1.6
