# api_yamdb
API для сервиса yamdb. Позволяет оценить произведение и оставить отзыв о нём.
## Технологии
Python 3.10, Django 3.2, DRF, JWT
## Как запустить
1. Клонируем репозиторий и переходим в него в командной строке

```
git clone https://github.com/QuiShimo/api_yamdb.git
```

```
cd api_yamdb
```

2. Создаем и активируем виртуальное окружение

```
python -m venv venv
```

```
source venv/Scripts/activate
```

3. Устанавливаем необходимые зависимости из requirements

```
pip install -r requirements.txt
```

4. Делаем миграции

```
python api_yamdb/manage.py migrate
```

5. Запускаем проект

```
python api_yamdb/manage.py runserver
```
## Примеры работы с API для всех пользователей

## Примеры работы с API для авторизованных пользователей
