# encontro_cadastro

Django app built for Encontro Febrafar. Staff register meetings (who meets
which pharmacy network, at which table and time) in the Django admin, and the
home page shows them as a board that refreshes every 5 seconds.

## Running locally

Requires Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export DJANGO_DEBUG=1
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The board is at http://127.0.0.1:8000/ and the admin at http://127.0.0.1:8000/admin/.

Run the tests with `DJANGO_DEBUG=1 python manage.py test`.

## Configuration

Settings that differ between machines come from environment variables:

| Variable | Purpose |
| --- | --- |
| `DJANGO_SECRET_KEY` | Required unless `DJANGO_DEBUG` is on. |
| `DJANGO_DEBUG` | `1` turns on debug mode. Never set it in production. |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated host names or IPs the site is served from, e.g. `example.com,203.0.113.10`. |

## Deploying

Generate a new secret key. The one that used to be committed in `settings.py`
is public and must not be reused.

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Set `DJANGO_SECRET_KEY` and `DJANGO_ALLOWED_HOSTS`, then run
`python manage.py migrate` and `python manage.py collectstatic`.
