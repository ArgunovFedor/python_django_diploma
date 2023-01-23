<div align="center">
    <h1>
        <a href="https://localhost:8080/">Megano</a>
    </h1>
    <h4>
        <a href="#links">Ссылки</a>
        •
        <a href="#roadmap">Roadmap</a>
        •
        <a href="#development-guide">Руководство по разработке</a>
        •
        <a href="#deployment">Деплой</a>
        •
        <a href="#contact">Контакты</a>
    </h4>
    <h3>
        <a href="https://vk.com/">
            <img src="https://img.shields.io/badge/maintainer-%40argunov_fm-yellow">
        </a>
        <a href="https://localhost:8080/">
            <img src="https://img.shields.io/website?url=http%3A%2F%2Fwww.triumphmayflowerclub.com%2F">
        </a>
        <a href="https://vk.com/">
            <img src="https://img.shields.io/badge/social-vk-darkred">
        </a>
    </h3>
</div>
Сайт по дипломной работе. 

## Table of contents

* [Links](#links)
* [Roadmap](#roadmap)
  * [Step1](#step-1)
  * [Features](#features)
  * [Technical](#technical)
* [Руководство по разработке](#guide)
  * [Запуск в локальной среде](#запуск-в-локальной-среде)
  * [Recommended tools](#recommended-tools)
* [Deployment](#deployment)
* [Contact](#contact)

## Roadmap
Это простой план действий для разработчиков представленный ввиде неполного списка.
## Step 1
- [x] Создание Django-проекта
- [x] Разработка модели хранения данных
- [x] Разработка структуры URL на сайте
- [x] Разработка каркаса приложения
- [x] Интеграция верстки шаблона сайта
- [x] Подключение административной панели и БД
- [x] Разработка верхнего меню и футера

### Content

### Features
- [x] Создать модели данных и сделать миграцию
- [ ] Сделать dockerfile и docker compose files для запуска в контейнере

## Guide
### Запуск в локальной среде
```shell
# создание виртуальной среды
python -m venv .venv
# активируем скрипт внутри папки .venv
# уставливаем зависимости из файла requirements.txt
pip install -r /path/to/requirements.txt
# делаем миграцию в бд
python manage.py migrate
# создаем суперюзера
python manage.py createsuperuser
# запускаем сервер (можно в аргументах указать конкретный порт)
python manage.py runserver
# теперь вы можете зайти на сайт и админку по дефолтному или указанному локальному порту
```
TODO: записать после создания docker файла
### Recommended tools
* Ide Pycharm
* Browser Chrome
## Deployment
TODO: записать процесс деплоя
## Contact
TODO: записать контакты