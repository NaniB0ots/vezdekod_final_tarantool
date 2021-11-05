# Сокращение ссылок
Ссылка на web интерфейс: http://tarantool.698865-cs07173.tmweb.ru/


## Запуск проекта 


Требуется `docker` и `docker-compose`


`$ docker-compose up -d --build`


_Проект запускается на порту 8081_


## Эндпоинты

**POST** `http://tarantool.698865-cs07173.tmweb.ru/set/`

Request:
```json
{
   "original_link": "https://vk.com"
}
```

Response [200]:
```json
   {
      "short_link": "http://tarantool.698865-cs07173.tmweb.ru/random_string",
      "qr_code": "img_in_base64"
   }
```


**GET** `http://tarantool.698865-cs07173.tmweb.ru/<random_string>/`

Response [302]:

Перенаправление на соответствующую оригинальную ссылку
