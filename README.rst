#############
flake8-slots
#############

.. start short_desc

**A Flake8 plugin to require __slots__ to be defined for subclasses of immutable types.**

.. end short_desc


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/flake8-slots/latest?logo=read-the-docs
	:target: https://flake8-slots.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/python-formate/flake8-slots/workflows/Docs%20Check/badge.svg
	:target: https://github.com/python-formate/flake8-slots/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/python-formate/flake8-slots/workflows/Linux/badge.svg
	:target: https://github.com/python-formate/flake8-slots/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/python-formate/flake8-slots/workflows/Windows/badge.svg
	:target: https://github.com/python-formate/flake8-slots/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/python-formate/flake8-slots/workflows/macOS/badge.svg
	:target: https://github.com/python-formate/flake8-slots/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/python-formate/flake8-slots/workflows/Flake8/badge.svg
	:target: https://github.com/python-formate/flake8-slots/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/python-formate/flake8-slots/workflows/mypy/badge.svg
	:target: https://github.com/python-formate/flake8-slots/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.repo-helper.uk/github/python-formate/flake8-slots/badge.svg
	:target: https://dependency-dash.repo-helper.uk/github/python-formate/flake8-slots/
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/python-formate/flake8-slots/master?logo=coveralls
	:target: https://coveralls.io/github/python-formate/flake8-slots?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/python-formate/flake8-slots?logo=codefactor
	:target: https://www.codefactor.io/repository/github/python-formate/flake8-slots
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/flake8-slots
	:target: https://pypi.org/project/flake8-slots/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/flake8-slots?logo=python&logoColor=white
	:target: https://pypi.org/project/flake8-slots/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/flake8-slots
	:target: https://pypi.org/project/flake8-slots/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/flake8-slots
	:target: https://pypi.org/project/flake8-slots/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/flake8-slots?logo=anaconda
	:target: https://anaconda.org/domdfcoding/flake8-slots
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/flake8-slots?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/flake8-slots
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/python-formate/flake8-slots
	:target: https://github.com/python-formate/flake8-slots/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/python-formate/flake8-slots
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/python-formate/flake8-slots/v0.1.6
	:target: https://github.com/python-formate/flake8-slots/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/python-formate/flake8-slots
	:target: https://github.com/python-formate/flake8-slots/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2023
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/flake8-slots
	:target: https://pypi.org/project/flake8-slots/
	:alt: PyPI - Downloads

.. end shields

Installation
--------------

.. start installation

``flake8-slots`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install flake8-slots

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels https://conda.anaconda.org/conda-forge
		$ conda config --add channels https://conda.anaconda.org/domdfcoding

	* Then install

	.. code-block:: bash

		$ conda install flake8-slots

.. end installation


Flake8 codes
--------------

============== =====================================================================
Code           Description
============== =====================================================================
SLOT000        Define __slots__ for subclasses of str
SLOT001        Define __slots__ for subclasses of tuple
SLOT002        Define __slots__ for subclasses of collections.namedtuple
============== =====================================================================


Use as a pre-commit hook
--------------------------

See `pre-commit <https://github.com/pre-commit/pre-commit>`_ for instructions

Sample ``.pre-commit-config.yaml``:

.. code-block:: yaml

	 - repo: https://gitlab.com/pycqa/flake8
	   rev: 3.8.1
	   hooks:
	    - id: flake8
	      additional_dependencies: [flake8-slots==0.1.6]
