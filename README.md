# YatubeAPI
## _Социальная сеть блогеров_

## Возможности
- Пиши посты в своём дневнике
- Подписывайся на других авторов
- Комментируй их посты
- Отправляй посты в сообщества


## Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:

```
HTTPS:
git clone https://github.com/Imwisagist/api_final_yatube
```
```
SSH:
git clone git@github.com:Imwisagist/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Документация:
После запуска на localhost доступна [документация].

## Примеры:
### Получение токена: 
* POST: http://127.0.0.1:8000/api/v1/jwt/create/ 
```
{
    "username": "string",
    "password": "string"
}
```
RESPONSE:
```
{
    "refresh": "string",
    "access": "string"
}
```

Для добавления/изменения данных через API необходимо добавить в header 
к запросу параметр 'Authorization' со значением 'Bearer ACCESS_TOKEN'.


### Получение публикаций (с офсетом и ограничением по количеству): 
* GET: http://127.0.0.1:8000/api/v1/posts/?offset=300&limit=100

RESPONSE:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

RESPONSE (при запросе без параметров offset и limit):
```
[
    {
        "id": 1,
        "author": "dmtr",
        "text": "dmtr post",
        "pub_date": "2022-07-28T12:19:43.288654Z",
        "image": null,
        "group": null
    }
]
```

### Создание публикации:

POST: http://127.0.0.1:8000/api/v1/posts/
```
{
  "text": "string",
  "image": "string", 
  "group": 0
}
# required only 'text', other fields is optional
```
RESPONSE:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Подписаться на автора (только для авторизованных пользователей):
POST: http://127.0.0.1:8000/api/v1/follow/
```
{
  "following": "string_username"
}
```
RESPONSE:
```
{
  "user": "string",
  "following": "string"
}
```

### Автор
*Дмитрий ImWisagist Спиряев* [Telegram] 


   [документация]: <http://127.0.0.1:8000/redoc/>
   [Telegram]: <https://t.me/Imwisagist>


