# Task Manager(Todolist)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-green)
![Html](https://img.shields.io/badge/html-orange)
![Bootstrap](https://img.shields.io/badge/Bootstrap-blue)
Task Manager - это веб-приложение, которое позволяет пользователям управлять своими задачами и сохранять их в ежедневнике. Приложение разработано на основе фреймворка Django и предоставляет функционал для создания, редактирования и удаления задач, а также просмотра детальной информации о каждой задаче.

## Установка и настройка

1. Установите Python и Django на свой компьютер, если они еще не установлены.

2. Склонируйте репозиторий приложения Task Manager:

```
git clone https://github.com/your_username/task-manager.git
```

3. Перейдите в директорию проекта:

```
cd task-manager
```

4. Установите зависимости:

```
pip install -r requirements.txt
```

5. Мигрируйте базу данных:

```
python manage.py migrate
```

6. Создайте суперпользователя (администратора):

```
python manage.py createsuperuser
```

7. Запустите сервер разработки Django:

```
python manage.py runserver
```

Приложение будет доступно по адресу `http://localhost:8000/`.

## Основной функционал

- Регистрация и вход в систему: пользователи могут создавать учетные записи и входить в систему с помощью своих учетных данных.

- Создание, редактирование и удаление задач: пользователи могут создавать новые
