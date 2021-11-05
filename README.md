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

![image](https://user-images.githubusercontent.com/56492378/140519304-5868c4cc-755f-45b4-8753-54a765698e7c.png)


**GET** `http://tarantool.698865-cs07173.tmweb.ru/<random_string>/`

Response [302]:

Перенаправление на соответствующую оригинальную ссылку

## Web интерфейс
![image](https://user-images.githubusercontent.com/56492378/140519544-587d0f94-274a-4514-9470-0545bf661c71.png)

