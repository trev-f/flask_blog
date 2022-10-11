# 01 - Getting started

[Python Flask Tutorial: Full-Featured Web App Part 1 - Getting Started](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

Run app:

## Run the app

Simple app startup:

```bash
export FLASK_APP=flaskblog
flask run
```

This is annoying because you have to restart the app every time changes are made in order to see the changes.
Running in debug mode solves this problem.

App startup in debug mode:

```bash
export FLASK_APP=flaskblog
export FLASK_DEBUG=1
flask run
```
