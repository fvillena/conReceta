FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /conreceta

COPY ./requirements.txt /conreceta/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /conreceta/requirements.txt

COPY ./conreceta /conreceta