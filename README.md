# Installing and running the hotel reservation API example

This repo is my version of the hotel reservation case study from the ArjanCodes Software Designer Mindset Course.

To make running the case study easy, you can install poetry to handle the dependencies. You can install poetry by running:

```bash
pip install poetry
```

Then, you can install the dependencies by running:

```bash
poetry install
```

To start the API server, run the following command:

```bash
poetry run uvicorn main:app --reload
```
