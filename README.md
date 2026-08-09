# REST API Automation Framework

## Overview

The project is API automation framework built with Python, pytest.

## Technologies

- Python
- pytest
- Requests
- REST API
- JSON
- GitHub Actions
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
git clone <your-repository-url>


## Run Tests 

### Locally

pytest -v

### With Docker

docker build -t jsonplaceholder-api-tests .
docker run --rm jsonplaceholder-api-tests