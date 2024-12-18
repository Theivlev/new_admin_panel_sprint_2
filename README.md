# Movie API Project

## Описание

Данный проект включает в себя два основных компонента: настройка окружения с помощью Docker и реализация API для выдачи информации о фильмах с использованием Django. 

### Структура проекта

1. **`docker_compose`**: Настройка Nginx, Docker и Django для обеспечения работы приложения в контейнеризованном окружении.
2. **`django_api`**: Реализация RESTful API для получения и обработки информации о фильмах.

### Функционал

- Настройка Docker-контейнеров для Python и PostgreSQL.
- Реализация API для:
  - Получения списка фильмов.
  - Получения информации о конкретном фильме по UUID.
  - Поддержка пагинации при выдаче списка фильмов.
  - Валидация данных с использованием JSON-схем.
  
### Используемые технологии

- [![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
- [![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
- [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
- [![Docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=Docker)](https://www.docker.com/)
- [![Nginx](https://img.shields.io/badge/-Nginx-464646?style=flat-square&logo=Nginx)](https://www.nginx.com/)
- [![uWSGI](https://img.shields.io/badge/-uWSGI-464646?style=flat-square&logo=uWSGI)](https://uwsgi-docs.readthedocs.io/)


### Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone <URL_репозитория>
   cd <папка_проекта>
