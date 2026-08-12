# REST API Automation Framework

## Overview

The project is API automation framework built with Python, pytest. The project can be executed locally or inside a Docker container to provide a consistent test environment.

## Technologies

- Python
- pytest
- Requests
- REST API
- JSON
- Docker

## Project Structure

api/
    base_api.py
    posts_api.py
    users_api.py
    logger.py

tests/
    test_posts.py
    test_users.py 

conftest.py
Dockerfile
requirements.txt

## Features

- GET request testing
- POST request testing
- PUT request testing
- DELETE request testing
- Positive and negative API testing
- Parameterized tests
- Request logging
- Reusable API classes

## Installation

Clone repository:

```bash
git clone https://github.com/KhatiaJeiranashvili/jsonplaceholder-api-testing.git
cd jsonplaceholder-api-testing
```


## Run Tests 

### Locally

pytest -v

### With Docker

Build the Docker image:

```bash
docker build -t jsonplaceholder-api-tests .
```

Run the tests:

```bash
docker run --rm jsonplaceholder-api-tests
```