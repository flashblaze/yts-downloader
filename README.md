# yts-downloader &middot; [![PyPI version shields.io](https://img.shields.io/pypi/v/yts-downloader.svg)](https://pypi.python.org/pypi/yts-downloader/) [![PyPI license](https://img.shields.io/pypi/l/yts-downloader.svg)](https://pypi.org/project/yts-downloader/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/yts-downloader.svg)](https://pypi.python.org/pypi/yts-downloader/) [![PyPI download total](https://img.shields.io/pypi/dm/yts-downloader.svg)](https://pypi.python.org/pypi/yts-downloader/)

Python CLI to download YTS movies using their API

# Tutorials and helpful content

1. [realpython](https://realpython.com/pypi-publish-python-package/)
2. [Demystefying Setuptools Entry Points](https://www.youtube.com/watch?v=0W0k6zP_Lto)
3. [Python Packaging from Init to Deploy](https://www.youtube.com/watch?v=4fzAMdLKC5k)

# Usage

`yts-downloader -h` for help

`yts-downloader <movie name>` to search for the movie in [yts.am](https://yts.am) database and download it.

eg: `yts-downloader 'aquaman'`

# Building

`python setup.py sdist bdist_wheel`

# Deploying on TestPyPI

`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

# Deploying on PyPI

`twine upload dist/*`

:tada: Live here: [yts-downloader](https://pypi.org/project/yts-downloader/) :tada:

Download via: `pip install yts-downloader`

**PS: I, in no way support piracy. This "tool" was created as a simple application of their API**
