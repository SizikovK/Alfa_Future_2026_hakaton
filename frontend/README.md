# Frontend

React, TypeScript и Vite. Общий env и Docker: [корневой README](../README.md).

## Локальный запуск

Требуется Node.js 24 LTS и npm. Из каталога `frontend`:

```bash
npm ci
npm run dev
```

По умолчанию сайт доступен на http://localhost:3000.
Vite читает порты из корневого `.env` и проксирует `/api` на локальный backend.
После изменения env перезапустите dev-сервер.

```bash
npm run lint          # ESLint
npm run format        # Prettier: форматирование
npm run check         # ESLint, Prettier и TypeScript
npm run build
npm run preview
```

`preview` проверяет статическую сборку, но не проксирует API.
Для проверки сборки вместе с API используйте Docker Compose.

`src/api` — клиент API, `src/components` — общие компоненты,
`src/features/chat` — будущий модуль чата, `src/styles` — общие стили.
Начальная страница очищена от логотипов, счётчика и демонстрационных стилей Vite.
В Docker Node собирает статику, Nginx раздаёт её и проксирует `/api`.
