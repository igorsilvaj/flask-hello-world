## If you want to run the application locally


1. Clone the repo
```sh
git clone git@github.com:igorsilvaj/flask-hello-world.git
```

2. Enter the folder
```sh
cd flask-hello-world
```
3. Create the Virtual Environment
```sh
python3 -m venv .venv && source .venv/bin/activate
```

4. Install the dependencies
```sh
python3 -m pip install -r requirements.txt
```

5. Start the application
```sh
flask run
```
or
```sh
gunicorn --pythonpath app src.flask_app.app:app
```
