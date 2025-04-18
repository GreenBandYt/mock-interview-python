# План реализации: Тренажёр для подготовки к МОК-интервью

## 1. Этапы и сроки

### Этап 1: Настройка окружения (1 день)
- Создать виртуальное окружение: `python3.13 -m venv .venv`.
- Установить зависимости: `fastapi`, `uvicorn`, `pydantic`, `aiogram`, `passlib`, `python-jose`, `jinja2`, `sqlalchemy`, `pymysql`, `python-dotenv`, `flake8`, `black`, `pytest`, `alembic`, `prometheus-fastapi-instrumentator`.
- Настроить MySQL сервер локально (Dev) и на Ubuntu 24.04 (Prod).

### Этап 2: База данных (1 день)
- Создать MySQL таблицы:
  - `interview_questions` (id, question, answer, level).
  - `users` (id, username, role, stats).
  - `admins` (id, username, hashed_password).
- Реализовать скрипт загрузки вопросов с уровнем "junior" in `data/load_questions.py`.

### Этап 2.5: Настройка инфраструктуры (1 день)
- Настроить `alembic` для миграций базы данных.
- Настроить логирование в `logs/app.log` с ротацией (DEBUG для dev, INFO для prod).
- Создать `.env.example`, `.env.dev`, `.env.prod` с настройками (например, `DATABASE_URL`, `BOT_TOKEN`).
- Создать `.gitignore` для исключения секретных данных, логов и временных файлов.

### Этап 3: API и веб (пользователи) (2 дня)
- Реализовать эндпоинты:
  - `GET /question/random?level={level}` — случайный вопрос.
  - `POST /answer/check` — проверка ответа.
  - `GET /stats?level={level}` — пользовательская статистика.
- Создать шаблоны:
  - `templates/user/index.html` — главная страница с выбором уровня.
  - `templates/user/stats.html` — статистика.

### Этап 4: Админ-панель (2 дня)
- Реализовать эндпоинты:
  - `POST /admin/login` — аутентификация.
  - `GET /admin/questions?level={level}` — список вопросов.
  - `POST /admin/questions` — добавление вопроса.
  - `PUT /admin/questions/{id}` — редактирование.
  - `DELETE /admin/questions/{id}` — удаление.
  - `GET /admin/users/stats?level={level}` — статистика пользователей.
  - `GET /admin/users/export` — экспорт в CSV.
- Защитить маршруты JWT-токенами.
- Создать шаблоны:
  - `templates/admin/index.html` — админ-панель.
  - `templates/admin/questions.html` — управление вопросами.
  - `templates/admin/users.html` — статистика пользователей.

### Этап 5: Telegram-бот (2 дня)
- Настроить вебхук: `POST /bot/webhook`.
- Реализовать пользовательские команды в `bot/handlers/user/user_handlers.py`:
  - `/question {level}` — случайный вопрос.
  - `/stats` — статистика.
- Реализовать админ-команды в `bot/handlers/admin/admin_handlers.py`:
  - `/admin_questions` — управление вопросами.
  - `/admin_stats` — статистика пользователей.

### Этап 5.5: Тестирование (1 день)
- Написать юнит-тесты в `tests/` для `core/`, `api/`, `bot/`.
- Проверить код на PEP 8 с помощью `flake8` и отформатировать с `black`.
- Добиться покрытия тестами не менее 80%.

### Этап 6: Тестирование и деплой (1 день)
- Локальный тест: `uvicorn main:app --reload`, проверка веб и бота.
- Prod: Настройка gunicorn, systemd, MySQL на Ubuntu 24.04.
- Настроить мониторинг через Prometheus.
- Проверить работу всех функций (веб, админ, бот).

### Этап 7: Документация (1 день)
- Добавить docstrings ко всем модулям, классам и функциям.
- Обновить `README.md` с инструкциями по запуску, настройке MySQL, переменных окружения и деплою.

## 2. Ресурсы
- Dev: Python 3.13, PyCharm 2024.3.4.
- Prod: Ubuntu 24.04, MySQL сервер.
- Разработчик: Опыт работы с MySQL и сервером.

## 3. Критерии завершения
- Все функции из ТЗ реализованы.
- Код протестирован локально и в продакшене.
- Покрытие тестами не менее 80%.
- Логи пишутся корректно, метрики доступны.
- Документация полная и понятная.