# Используем базовый образ Python
FROM python:3.11-slim
# Устанавливаем рабочую директорию в контейнере
WORKDIR /app
# Копируем зависимости в контейнер
COPY requirements.txt .
# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
# Копируем код проекта в контейнер
COPY . .
# Устанавливаем переменную окружения для Django
ENV PYTHONUNBUFFERED 1
# Выполняем миграции и запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
