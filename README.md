<h1 align="center">
    Translation Management
</h1>

<h4 align="center">A Translation Task Management tool to help track the ongoing work in the translation department.</h4>

## Overview

This is a pet project based on the real needs. As a Translation Manager and the translation process coordinator, I needed a tool capable of tracking the ongoing translation / review tasks and tailored for the specific project and its peculiarities.

This is a **work in progress**. The aim is to have a tool that would have:

- A web interface to input the tasks and track their progress
- An API for an external service like a mobile app

## Technology

-   Python 3.9.8
-   Django 4.0.6
-   Django Rest Framework 3.13.1
-   SimpleJWT
-   Unittest
-   SQLite3

## Installation

```bash
# Clone the repo and cd to it in the Terminal:
$ git clone https://github.com/ilyakutilin/translation_management.git
$ cd translation_management

# Create and activate a virtual environment:
$ python3 -m venv env
$ source env/bin/activate

# Install the dependencies:
$ python3 -m pip install --upgrade pip
$ pip install -r requirements.txt

# Perform the migrations:
$ python3 manage.py migrate

# Launch the dev server:
$ python3 manage.py runserver
```

