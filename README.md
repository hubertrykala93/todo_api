## Installation

Install Python 3.10 and clone the GitHub repository.

```bash
git clone https://github.com/hubertrykala93/todo_api.git
cd todo_api
```

Set up a virtual environment.

```bash
python3.10 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
(venv) pip3 install -r requirements.txt
```

Create a PostgreSQL database.

```bash
psql -U postgres
CREATE DATABASE todo_api;
```

Configure database settings.

DATABASE_NAME</br>
DATABASE_USER</br>
DATABASE_PASSWORD</br>
DATABASE_HOST</br>
DATABASE_PORT

For example:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo_api',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Apply migrations.

```bash
(venv) python3 manage.py makemigrations
(venv) python3 manage.py migrate
```

Load initial data.

```bash
(venv) python3 manage.py loaddata data/taskstatuses.json
(venv) python3 manage.py loaddata data/taskpriorities.json
```

Run the development server.

```bash
(venv) python3 manage.py runserver
```
