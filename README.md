# Pokémon Project

## Description

A simple Pokémon project built with Django. My idea is to create a project to practice my python/django skills,
some React as well.

As for what the project does: is simple web app that lets users browse,
view details, and store Pokémon from the PokéAPI.

🔍 Features so far:
✅ Fetches Pokémon data (name, types, image) from the PokéAPI.
✅ Saves Pokémon locally to avoid duplicate API calls.
✅ Shows a list of Pokémon with names, images, and types.
✅ Lets users click for a detail view of any Pokémon.
✅ Has an admin panel to manage Pokémon, favorites, tags, and notes.
✅ Has a frontend built with React and TypeScript.
✅ Has a backend built with Django.
✅ Has a database built with SQLite.


## Requirements

for backend:
- Python > 3.9.10
- pyenv if you want a python version manager
- Django 4.2.21
- requests 2.32.3

for frontend:
- nodejs > 18, currently using 22.10.0
- npm
- vite
- typescript
- nvm (optional) if you have multiple node versions

## Installation

```bash
python -m venv venv
source venv/bin/activate if you are using mac
pip install -r requirements.txt

python manage.py runserver to start the API server
npm run dev to start the frontend server, API server must be running
```


## Disclaimer

This project is for my educational personal purposes only.

Made with a bunch of ❤️ and curiosity by [Julieth Sarmiento](https://github.com/JulieSarmiento)

