FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

COPY . /code
WORKDIR /code

RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

EXPOSE 8000

CMD [ "pipenv", "run", "server" ]