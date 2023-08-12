# Task Manager(Todolist)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-green)
![Html](https://img.shields.io/badge/html-orange)
![Bootstrap](https://img.shields.io/badge/Bootstrap-blue)
Task Manager - это веб-приложение, которое позволяет пользователям управлять своими задачами и сохранять их в ежедневнике. Приложение разработано на основе фреймворка Django и предоставляет функционал для создания, редактирования и удаления задач, а также просмотра детальной информации о каждой задаче. Присутсвует регистрация и авторизация пользователей. У каждого юзера свой ежедневник, один не имеет доступа к другому. Переходы через адресную строку тоже заблокированы, написаны методы сортировки и более подробно можно узнать, открыв код проекта.

![Снимок](https://github.com/AluHadj22/TaskManager/assets/140946881/c40f0c13-5946-4635-b78c-89f01cb3d4d1)

![Снимо2к](https://github.com/AluHadj22/TaskManager/assets/140946881/e30162e4-9952-4005-8897-cb6fbe41e071)

![Сним3ок](https://github.com/AluHadj22/TaskManager/assets/140946881/e68a8a43-e0b4-45a7-a996-9624c5b4f0f5)

![Снимок4](https://github.com/AluHadj22/TaskManager/assets/140946881/665c416e-39d9-4dd2-8ac3-4c5cc6abd32f)

![Сним5ок](https://github.com/AluHadj22/TaskManager/assets/140946881/7db9f8d3-6d93-4438-8f4a-db3d1144d086)

![Сним6ок](https://github.com/AluHadj22/TaskManager/assets/140946881/59e69855-ef26-42ff-ac1b-23d2d9ecfcbc)




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

- Создание, редактирование и удаление задач: пользователи могут создавать новые, удалять старые и изменять.
