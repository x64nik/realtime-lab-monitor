FROM python:3.11-slim as base
WORKDIR /app
COPY requirements.txt .
RUN python -m venv /venv
RUN /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

FROM python:3.11-slim AS runtime
WORKDIR /backend
COPY --from=base /venv /venv
COPY ./app ./app
COPY .env ./app/
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
CMD [ "fastapi", "run", "app/main.py" ]