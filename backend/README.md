# Running App

You need install uv for this project.

> To running the app, you must execute the following command to generate the Django secret key.

```python
uv run python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Copy the key that the command gives you and paste it into .env file in a variable called SECRET_KEY='' and below it put DEBUG=True variable.

After these commands:
- uv sync (to synchronize the packages)
- uv run manage.py makemigrations
- uv run manage.py migrate

Then run uv run manage.py runserver.