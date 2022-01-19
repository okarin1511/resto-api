# resto-api
## To get started

### 1. Clone the repository

```
git clone git@github.com:<username>/resto-api.git
cd inventory_api
```

### 2. Setup Project

1. Install the virtualenv tool and create a virtual environment

```
pip install virtualenv
virtualenv env
```

2. Install the dependencies

```
pip install -r requirements.txt
```

3. Run the migrations

```
python manage.py makemigrations
python manage.py migrate
```

4. Finally, run the server

```
python manage.py runserver
```

### 3. Task 1: Database entry

To execute the db entry script, go inside the `utils` sub directory and run the `dbentry.py` file

```
cd utils
python dbentry.py
```
