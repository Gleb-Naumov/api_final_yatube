# API YATUBE 
## Проект предназначем для: просмотра постов, подписки на авторов. Так же вы сможете оставлять комментарии под постами. В проекте реализована аутентификация по JWT токену. Настоены разрешения, под разные эндпоинты. Есть возможность добавлять картинки.
Стек: Python, Django, Django REST Framework, djoser, simpleJWT, git

# Если вы хотите развернуть проект на локальной машине, вам нужно выполнить следующие действия:
- ### Зайти на github и скачать репозитопий **https://github.com/Gleb-Naumov/api_final_yatube**
- ### Создать виртуальное окружение ``` py -3.9 -v venv venv ```
- ### Активировать виртуальное окружение ``` source venv/Script/activate```
- ### Установить зависимости ``` pip install -r requirements.txt ```
- ### Выполнить миграции ``` python manage.py migrate ```
- ### Включить сервер ``` python manage.py runserver ```


## Для того что-бы пользоваться всеми благами нашего API вам нужно сначала загерестрироваться: 
### Для того чтобы зарегестрироваться вам нужно зайти на эндпоинт(**ОБЯЗАТЕЛЬНО метод запроса должен быть POST**) **http://127.0.0.1:8000/api/v1/auth/jwt/users/** в теле запроса указать *username* и *password*. После регистрации вам нужно получить свой jwt ключ, его можно получить на эндпоинте(**ОБЯЗАТЕЛЬНО метод запроса должен быть POST**) **http://127.0.0.1:8000/api/v1/auth/jwt/create/**  в теле запроса нужно будет так же передать *username* и *password*. После этих действий в теле запроса будет указано 2 ключа, вам нужен ключ  с названием *access*.
### Передавайте этот ключ в заголовок в поле значение. Перед ключем должно быть слово Bearer и пробел, а потом уже ключ.
