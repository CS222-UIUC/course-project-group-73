# Windows:

Two terminals:

Startup the backend:

```
cd flask-server
python -m venv venv
venv\Scripts\activate
pip install flask
python server.py
http://localhost:5000/members
```

Startup the frontend:

```
cd client
npm start
```

backend proxy runs on localhost:5000 (configured in package.json file)
