[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=Docker)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/-Nginx-464646?style=flat-square&logo=Nginx)](https://www.nginx.com/)
[![uWSGI](https://img.shields.io/badge/-uWSGI-464646?style=flat-square&logo=uWSGI)](https://uwsgi-docs.readthedocs.io/)

# Сервис Movie API Project

## Описание

Данный проект включает в себя два основных компонента: настройка окружения с помощью Docker и реализация API для выдачи информации о фильмах с использованием Django. 

### Функционал

- Настройка Docker-контейнеров для Python и PostgreSQL.
- Реализация API для:
  - Получения списка фильмов.
  - Получения информации о конкретном фильме по UUID.
  - Поддержка пагинации при выдаче списка фильмов.
  - Валидация данных с использованием JSON-схем.

### Технологии

- Python 3.12
- Docker
- PostgreSQL
- uWSGI

## Установка и запуск

1. - Склонировать репозиторий:

```bash
    git clone <название репозитория>
```

2. - Убедитесь, что на вашем устройстве установлены Docker и Docker Compose.

3. - Создайте .env файлы на том же уровне .env.example

  ```bash
    cp .env.example .env
  ```

4. - Постройте и запустите контейнеры с помощью Docker Compose:
    ```bash
      docker-compose up --build
     ```

5. - Суперюзер

      login: admin
      password: 123123
   

6. - Админ-панель доступна по адресу http://localhost/admin/

## API документация

### Общая информация

Версия API: v1  
Базовый URL: http://localhost/api/v1/

### Эндпоинты

#### Список фильмов
```
GET - '/movies/ '
```
Пример успешного ответа:

```json
{
  "count": 1000,
  "total_pages": 20,
  "prev": 1,
  "next": 2,
  "results": [
    {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "title": "Crescent Star",
      "description": "In 1944, the Germans began rounding up the Jews of Rhodes.",
      "creation_date": "2024-12-19",
      "rating": 7.9,
      "type": "movie",
      "genres": ["Drama", "Short"],
      "actors": ["Darrell Geer", "Michael Bond"],
      "directors": ["Turgut Turk Adiguzel"],
      "writers": ["Turgut Turk Adiguzel"]
    }
  ]
}
```
#### Информация о фильме


```
GET - '/movies/{id}/ '
```
Пример успешного ответа:

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "title": "Crescent Star",
  "description": "In 1944, the Germans began rounding up the Jews of Rhodes.",
  "creation_date": "2024-12-19",
  "rating": 7.9,
  "type": "movie",
  "genres": ["Drama", "Short"],
  "actors": ["Darrell Geer", "Michael Bond"],
  "directors": ["Turgut Turk Adiguzel"],
  "writers": ["Turgut Turk Adiguzel"]
}
```
