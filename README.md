# Django To-Do Application

This project is a simple to-do application built with Django. It allows users to add, edit, and delete tasks from a to-do list. The setup includes a Docker container and a ```docker compose``` to automate the environment setup, making it easy to get the application to run locally.

## Features

- Add tasks with descriptions and due dates
- View tasks
- Delete tasks

## Getting Started

Follow these instructions to get a copy of the project running on your local machine.

### Prerequisites

- *Docker* and *Docker Compose* installed
- Basic knowledge of *Django*
- VSCode (My Recommendation)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/tiefaul/todo_website.git
```

2. Create a .env file:

```bash
touch .env
```

use the ```example.env``` as a template to configure your ```.env```. you must specify your IP address and Django secret_key. which I will show you how to generate in the next step

3. Generate a Django Secret_Key

Open a terminal and run python.

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Copy the secret key and paste it into your .env file.

4. Create the SQLite database

```python
python manage.py migrate
```

5. Run the server

```bash
docker-compose up -d
```

6. Open your browser and navigate to <http://localhost> or whatever IP you used for the ```.env``` file.
