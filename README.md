# Typograf Service

This script helps to prepare the text before publication.

# What it's doing?

- replaces the qoutes `"`, `'` to `«` `»`
- replaces hyphens with *em dashes* where it's need
- in a phone number inserts *en dashes*
- removes extra white spaces and transfer lines
- binds the number of subsequent words with a nonbreaking space
- binds the Union and any words of 1-2 characters with subsequent words

# How to install

Use Venv or virtualenv for insulation project. Virtualenv example:

```
$ python virtualevn myenv
$ source myenv/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```

Export the FLASK_APP environment variable:

```
$ export FLASK_APP=server.py
$ flask run
 * Running on http://127.0.0.1:5000/
```
Click on the [link](http://127.0.0.1:5000/)

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
