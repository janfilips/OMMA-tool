# OMMA-tool

### Online Mechanical Measurement Analysis

Dive into the future of mechanical measurement analysis with OMMA-tool. Simplify your workflow, enhance accuracy, and streamline your processes, all in one place.

## Local Development

Get your hands dirty with the local setup and feel the power of OMMA-tool in your local environment. Follow these steps to get started:

1. Set Up the Python Virtual Environment

Make sure you have Python 3.11 installed, then create and activate a virtual environment:

```
python3.11 -m venv .venv
source .venv/bin/activate
````

2. Environment Variables

Copy .env.devel to .env for development settings:

```
cp .env.devel .env
````

3. Load the environment variables:

```
export $(grep -v '^#' .env | xargs)
```

4. Dependency Installation

With Poetry, installing dependencies is a breeze:

```
poetry install
```

Unleash the power of OMMA-tool locally with uvicorn:

```
poetry run uvicorn backend.main:app --port 8000 --log-level info --reload
```

Visit http://localhost:8000 in your browser and you're up and running!


## Tests

To run tests, simply run pytest.

```
OMMA-tool % pytest
==================================== test session starts ====================================
platform darwin -- Python 3.11.0, pytest-8.0.1, pluggy-1.4.0
rootdir: /Users/margaretka/code/OMMA-tool
plugins: anyio-4.3.0
collected 1 item
tests/test_api.py .                                                                   [100%]
===================================== 1 passed in 1.80s =====================================
```


## Docker

Prefer to keep things neat with Docker? We've got you covered. Spin up the project with a few simple commands:

Build the Container and start them in the background:

```
docker compose build --no-cache
docker compose up -d
docker compose logs -f
```


## Production Checklist

[ ] triple-check .env
[ ] XXX TODO...
