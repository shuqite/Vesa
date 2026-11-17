# install slim python
FROM python:3.12-slim

# build essentials
RUN apt-get update && \
    apt-get install -y build-essential

WORKDIR /app

# Install requirements
RUN pip install --no-cache-dir poetry
ENV POETRY_VIRTUALENVS_CREATE=false
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-ansi --no-root --no-directory

COPY Images/ ./Images
COPY main.py ./
COPY src/ ./src/

CMD ["python", "main.py"]
