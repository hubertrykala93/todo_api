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

Configure database settings. For example:

```
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

## Api Reference

Api Response Structure

```json
{
  "message": "string",
  "success": "boolean",
  "data": "object or list"
}
```

Response Codes

| HTTP Code | Meaning                  | Description                                    |
|-----------|--------------------------|------------------------------------------------|
| 200       | OK                       | The request was successful.                   |
| 201       | Created                  | A new resource was successfully created.      |
| 400       | Bad Request              | The request was invalid or malformed.         |
| 401       | Unauthorized             | Authentication is required and has failed.    |
| 403       | Forbidden                | You do not have permission to access this.    |
| 404       | Not Found                | The requested resource could not be found.    |
| 500       | Internal Server Error    | An unexpected error occurred on the server.   |


Endpoints

| HTTP Method      | URL                        | Description                                         |
|------------------|----------------------------|-----------------------------------------------------|
| GET/POST         | api/v1/taskstatuses        | Retrieve all task statuses or create a new task status.                         |
| GET/PATCH/DELETE | api/v1/taskstauses/{id}    | Retrieve, update, or delete a specific task status by ID.  |
| GET/POST         | api/v1/taskpriorities      | Retrieve all task priorities or create a new task priority.                       |
| GET/PATCH/DELETE | api/v1/taskpriorities/{id} | Retrieve, update, or delete a specific task priority by ID. |
| GET/POST         | api/v1/tasks               | Retrieve all tasks or create a new task.                                 |
| GET/PATCH/DELETE | api/v1/tasks/{id}          | Retrieve, update, or delete a specific task by ID.         |