# Notion Lite

A stripped-down Notion clone I built to learn full-stack development with FastAPI and React. It does the basics — create pages, write stuff in them, edit them, delete them. Nothing more.

## Stack

- **Backend** — FastAPI + PostgreSQL + SQLAlchemy
- **Frontend** — React + Vite + Tailwind CSS
- **Infrastructure** — Docker + Docker Compose

## Running it

Make sure you have Docker installed, then:

```bash
docker compose up --build
```

Frontend runs on `http://localhost:3000`, backend on `http://localhost:80`.

You'll need a `.env` file in the root:

```
DATABASE_URL=postgresql://postgres:<your_password>@db:5432/postgres
POSTGRES_PASSWORD=<your_password>
```

## API

| Method | Endpoint | What it does |
|--------|----------|--------------|
| GET | `/pages` | list all pages |
| POST | `/pages` | create a page |
| GET | `/pages/{id}` | get one page |
| PUT | `/pages/{id}` | update a page |
| DELETE | `/pages/{id}` | delete a page |

## Project structure

```
app/
  config.py       # env config
  database.py     # db session setup
  models/         # SQLAlchemy models
  schemas/        # Pydantic schemas
  routes/         # API endpoints
  services/       # business logic
frontend/
  src/
    api/          # all fetch calls live here
    App.jsx       # main UI
```
