## Installation

Install Python 3.10 and clone the GitHub repository.

```bash
$ git clone https://github.com/hubertrykala93/todo_api.git
$ cd todo_api
```

Create a virtual environment to install dependencies in and activate it:

```bash
$ python3.10 -m venv venv
$ source venv/bin/activate
```

Install the dependencies:

```bash
(venv)$ pip3 install -r requirements.txt
```

Create a new PostgreSQL database.

```bash
psql -U postgres
```

```bash
CREATE DATABASE todo_api;
```

Set the data for your local PostgreSQL database in settings/settings.py.

DATABASE_NAME</br>
DATABASE_USER</br>
DATABASE_PASSWORD</br>
DATABASE_HOST</br>
DATABASE_PORT

Run migrations.

```bash
(venv)$ python3 manage.py migrate
```

Import the data into PostgreSQL.

```bash
(venv)$ python3 manage.py loaddata data/taskstatuses.json
(venv)$ python3 manage.py loaddata data/taskpriorities.json
```

Run the project.

```bash
(venv)$ python3 manage.py runserver
```

And then navigate to ```http://127.0.0.1:8000``` or ```http://localhost:8000```.
