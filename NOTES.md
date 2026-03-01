# Spell Caster — Project Notes

## Origin & Motivation

Started as a brainstorming exercise to find a learning project that would:
- Build transferable skills for a data engineering day job (healthcare domain)
- Teach API design and infrastructure from the ground up (not just consuming pre-built components)
- Be intrinsically motivating enough to avoid procrastination

A PL football data platform was considered but rejected because it would mostly involve consuming and reproducing someone else's API structure — pipeline-shaped work already present in the day job. A TTRPG tool won because it forces you to **design the domain model yourself**, which is the harder and more instructive problem.

## The Problem Being Solved

The group plays D&D 5e (2024 revision). Most players are new and all are spellcasters. Core friction points:
- Overwhelmed by the volume of spell options during play and on level-up
- Decision paralysis from trying to make the "optimal" choice
- Sharing a single physical PHB across the table
- Difficulty tracking what they're actually capable of in the moment

The root issue is not missing information — it's **too much information in the wrong shape** for the context. The PHB presents all options equally; players need options narrowed by situation.

## What the Tool Does

A shared browser-based spell companion (phone-friendly) with:
- **Player profiles** tracking current spell list and spell slot state
- **Situational filtering** — players choose intent (damage / buff / control), target shape (single / AoE), range, concentration status
- **Plain-language spell summaries** — not raw RAW text, but readable descriptions
- **Spell slot tracking** — mark slots spent during a session, reset on rest
- **Comparison mode** — side-by-side spell options when leveling up

The spell dataset will be built manually to cover the 2024 revision (structured open data for 2024 is sparse). This means **spell categorisation (damage vs control vs buff) is a deliberate design decision**, not imported metadata.

## Tech Stack & Rationale

| Layer | Choice | Why |
|---|---|---|
| API | FastAPI (Python) | Clean, modern, forces schema thinking, good for learning API design |
| Database | PostgreSQL | Fits the relational data model, familiar territory from data engineering |
| Containerisation | Docker + Compose | Infrastructure learning from day one, not as an afterthought |
| Package management | uv | Modern Python tooling, fast |
| Hosting | AWS (TBD) | Main infrastructure learning goal |
| Frontend | Deferred | Minimal experience; focus on API and infrastructure first |

Frontend will be the simplest viable thing — likely minimal HTML served by FastAPI itself — until the backend is solid and there's motivation to invest further.

## Current State

Project skeleton is in place and runnable:

```
spell-caster/
├── app/
│   ├── __init__.py
│   └── main.py           # single /health route
├── pyproject.toml
├── .python-version       # 3.13
├── Dockerfile
├── docker-compose.yml    # api + postgres, with healthcheck and hot reload
└── .env.example
```

Start with:
```bash
cp .env.example .env
docker compose up --build
```

- `http://localhost:8000/health` — health check
- `http://localhost:8000/docs` — auto-generated interactive API docs

## Next Steps (Not Yet Started)

- Design the data model: spell schema, profile schema, spell slot state
- Decide on the tagging/categorisation system for spells (the "judgement" layer)
- Connect FastAPI to PostgreSQL (SQLAlchemy or raw psycopg)
- First real routes: CRUD for spells, CRUD for profiles
- Begin populating the spell dataset
