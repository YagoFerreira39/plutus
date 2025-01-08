FROM python:3.11-alpine
COPY . .

ENV PATH=/root/.local:$PATH
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Install necessary packages
RUN apk add --no-cache curl libc6-compat
RUN apk add --update bash

CMD ["python3", "main.py"]