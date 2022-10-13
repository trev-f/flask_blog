# 05 - Package structure

[Python Flask Tutorial: Full-Featured Web App Part 5 - Package Structure](https://www.youtube.com/watch?v=44PvX0Yv368)

## `__init__.py`

The [`__init__.py`](../flaskblog/__init__.py) file here seems kind of contrived and goes against my preferred usage of `__init__.py` files which is to either leave them blank or use them for APIs and nothing else.
I may consider refactoring this when I build my own Flask apps.
In general I'm not a huge fan of this restructuring, but it is much better than leaving things in a single file.

## `run.py`

This video is 3-4 years old by the time I've stumbled across it, but I think the current convention is to run the app from a file called `app.py`.
This is of course minor, but I would prefer to stick to current conventions where possible.
