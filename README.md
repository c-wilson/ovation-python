# Ovation Python API


Ovation is the powerful data management service engineered specifically for scientists that liberates research through organization of multiple data formats and sources, the ability to link raw data with analysis and the freedom to safely share all of this with colleagues and collaborators.

The Ovation Python API wraps the Ovation Java API for use by CPython. Through this Python API, CPython users can access the full functionality of the Ovation ecosystem from within Python. 

Jython users can access the Ovation Java API directly and should *not* use this Python API.


## Requirements

* [Java](http://www.oracle.com/technetwork/java/javase/downloads/index.html) 1.7+
* CPython 2.7.x or 3.4+

## Installation

Install the `ovation` package from [PyPI](http://pypi.python.org):

	pip install ovation


### Windows

VS2008 Runtime: http://www.microsoft.com/en-us/download/details.aspx?id=29

Install Cython, NumPy, Scipy binaries from http://www.lfd.uci.edu/~gohlke/pythonlibs/#cython


Add to Path:

	C:\Program Files\Java\[jre7]\bin\client
	C:\Program Files\Java\[jre7]\bin\client


## Usage


### Connecting to the Ovation database

	>> from ovation.connection import new_data_context
	>> context = new_data_context(<ovation.io user email>)
	Ovation password: <ovation.io password>
	>> projects = list(context.getProjects())
	




