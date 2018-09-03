Manage your library easily.
=================================

<img src=".github/Selection_016.png" alt="Overview"/>
<img src=".github/Selection_017.png" alt="Overview"/>
<img src=".github/Selection_018.png" alt="Overview"/>
<img src=".github/Selection_019.png" alt="Overview"/>

## Run.

*Pipenv* is used. `python-decouple` is also used for the configuration, thus, you can use a `.env` file instead of
environment variables.

```
pipenv install
DJANGO_SECRET_KEY=supersecretkey python manage.py migrate
DJANGO_SECRET_KEY=supersecretkey python manage.py createsuperuser # to have access to the admin page.
DJANGO_SECRET_KEY=supersecretkey python manage.py runserver
```

By default, a sqlite3 database is used. You can change it by using different parameters:
- `DATABASE_ENGINE`: see django documentation, default to sqlite3
- `DATABASE_NAME`: database name, default to `.data/db.sqlite3`
- `DATABASE_URL`: database URL, default to `None` (must be `None` for SQLite3)
- `DATABASE_PORT`: the database port, default to `None` (must be `None` for SQLite3)
- `DATABASE_USER`: the database user, default to `None` (must be `None` for SQLite3)
- `DATABASE_PASSWORD`: the database password, default to `None` (must be `None` for SQLite3)

## Deploy using Docker

**Not yet available on DockerHub.**
```bash
docker run -it --name rlibrary \
  -p 8000:8000 \
  -e "DJANGO_SECRET_KEY=supersecretkey" dannywillems/rlibrary
```

You can also specify the different variables listed above to use a different database.