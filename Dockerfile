FROM python:3.6

COPY . /usr/src/app
RUN rm -f **/*.sqlite3
WORKDIR /usr/src/app
RUN mkdir -p .data

RUN pip install pipenv
RUN pipenv install --deploy
RUN pipenv run python manage.py collectstatic

EXPOSE 8000

CMD pipenv run python manage.py migrate && /usr/src/app/start.sh