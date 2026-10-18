# AI Chat

Сервис чата с ИИ агентом: FastAPI / Python и React / TypeScript / Vite.
Сейчас реализован каркас проекта и health endpoint; агент и чат ещё не подключены.

## Запуск в Docker

Требуются Docker и Docker Compose.

```bash
cp .env.example .env
docker compose up --build -d
```

- Сайт: http://localhost:3000
- API через сайт: http://localhost:3000/api/health
- API напрямую: http://localhost:8000/api/health
- Swagger: http://localhost:8000/api/docs

Порты указаны для настроек по умолчанию. Остановка: `docker compose down`.
Логи: `docker compose logs -f`. После изменения кода повторите запуск с `--build`.
Compose поднимает ровно два контейнера: FastAPI и Nginx со сборкой React.
Nginx направляет `/api/*` в backend. Отдельный контейнер Node не требуется.

## Конфигурация

Общий `.env` находится в корне и не коммитится. `.env.example` содержит шаблон.
`FRONTEND_PORT`, `BACKEND_PORT` задают внешние порты;
`APP_ENV`, `LOG_LEVEL`, `LLM_API_KEY`, `LLM_MODEL` передаются бэкенду.
Настройки LLM зарезервированы для будущей интеграции.
Ключи провайдера не передаются фронтенду. Адрес API в браузере — `/api`.
Для применения env к контейнерам повторите `docker compose up -d`.

## Разработка без Docker

Сначала скопируйте `.env.example` в `.env`, затем запустите оба проекта
в разных терминалах: [backend](backend/README.md), [frontend](frontend/README.md).

## Структура

- `backend/` — API, конфигурация, схемы, сервисы, тесты.
- `frontend/` — React-приложение, клиент API, компоненты и функции чата.
- `compose.yaml` — совместный запуск.

## Команды разработки

Требуются GNU Make, Python 3.13+, Node.js 24 и npm. Из корня проекта:

```bash
make install           # зависимости обоих проектов, включая dev-инструменты
make install-back      # только Python, создаёт backend/.venv
make install-front     # только frontend, npm ci
make check             # Ruff, ESLint, Prettier и TypeScript
make format            # автоисправление Ruff и форматирование Ruff / Prettier
make test              # Python-тесты через Invoke / pytest
```

Для отдельных проектов доступны `make check-back`, `make check-front`,
`make format-back`, `make format-front`. Справка: `make help`.
Python-интерпретатор установки можно выбрать: `make install-backend PYTHON=python3.13`.
