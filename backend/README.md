# Backend

Python 3.13+, FastAPI. Общая конфигурация: [корневой README](../README.md).

## Локальный запуск

Из каталога `backend`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

При изменении `BACKEND_PORT` в корневом `.env` укажите тот же порт в `--port`.
Приложение читает корневой `.env` через pydantic-settings; переменные окружения
имеют приоритет. В Docker конфигурацию передаёт Compose.

- `GET /api/health` → `{"status":"ok"}`
- `/api/docs` — Swagger UI.

## Проверки

```bash
inv check    # Ruff: линтер и проверка форматирования
inv format   # автоисправление Ruff и форматирование
inv test     # pytest
```

`app/main.py` создаёт приложение, `api/routes` содержит маршруты,
`core/config.py` — конфигурацию, `schemas` — модели данных,
`services` — бизнес-логику. Файлы чата и агента пока являются заготовками.
Зависимости приложения: `requirements.txt`; инструменты: `requirements-dev.txt`.

Команды `inv` запускаются из `backend` с активированным `.venv`.
Из корня доступны `make install-back`, `make check-back`,
`make format-back` и `make test` без ручной активации окружения.
