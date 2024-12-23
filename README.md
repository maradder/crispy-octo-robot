# Simple Flask App

## App Structure

```bash
.
├── ./app
│   ├── ./app/app.py
│   ├── ./app/__init__.py
│   └── ./app/routes
│       ├── ./app/routes/__init__.py
│       └── ./app/routes/world.py
├── ./app_structure.txt
├── ./README.md
└── ./requirements.txt
```

## Install Dependencies

```bash
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

## Run the App

```bash
export FLASK_APP=app

flask run
```
