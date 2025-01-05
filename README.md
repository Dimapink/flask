# Домашние задание по Flask

## Описание

API сервис по созданию, редактированию, удалению объявлений.

Реализованы следующие методы:

```GET /adv/{id}``` - получить объявление

```POST /adv``` - опубликовать объявление, пример запроса (owner - необязательное поле):
```json
{
	"title": "New",
	"description": "Some text",
    "owner": "Some owner"
}
```
```DELETE /adv/{id}``` - удалить объявление

```PATCH /adv/{id}``` - обновить объявление



## Как запустить

### Dependencies

* Python 3.10 - 3.12 
* Poetry 1.7.1

### Запуск локально (для отладки и пр.)

* ```poetry install --no-root```
* ```poetry shell```
* ```export POSTGRES_PASSWORD={пароль от пользователя postgres БД}```
* ```poetry run python src.service.py```

### Запуск полностью в контейнерах

* Создать .env файл в корне проекта с переменными
```bash
DB_USER=postgres
DB_NAME=postgres
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```

* ```docker-compose up -d```
