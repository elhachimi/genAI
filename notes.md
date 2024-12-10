# FastAPI project structures

1. Flat
2. Nested
3. Modular
4. Onion/Layered

## Flat

<pre>
flat-project/
├── app/
│ ├── services.py
│ ├── database.py
│ ├── models.py
│ ├── routers.py
│ └── main.py
├── requirements.txt
├── .env
├── .gitignore
</pre>

## Nested

<pre>
nested-project/
├── app/
│ ├── main.py
│ ├── dependencies.py
│ └── services
│ │ ├── users.py
│ │ └── profiles.py
│ └── models
│ │ ├── users.py
│ │ └── profiles.py
│ └── routers
│ ├── users.py
│ └── profiles.py
├── requirements.txt
├── .env
├── .gitignore
</pre>

## Modular

<pre>
modular-project
├── app
│ └── modules
│ │ ├── auth
│ │ │ ├── routers.py
│ │ │ ├── models.py
│ │ │ ├── dependencies.py
│ │ │ ├── services.py
│ │ └── users
│ │ │ ├── router.py
│ │ │ ├── models.py
│ │ │ ├── dependencies.py
│ │ │ ├── services.py
│ │ └── profiles
............
│ ├── settings.py # global configs
│ ├── models.py # global models
│ ├── exceptions.py # global exceptions
│ └── main.py
├── requirements.txt
├── .env
├── .gitignore
</pre>
