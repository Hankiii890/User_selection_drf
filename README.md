# Django Project with Docker

## Описание

Этот проект представляет собой приложение на Django, использующее Docker для контейнеризации. Приложение включает в себя PostgreSQL в качестве базы данных и Redis для кэширования.

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone <URL моего репозитория>
   cd <название деректории моего проекта>

2. **Создайте и активируйте виртуальное окружение:**
    ```bash
   python -m venv myenv
   source myenv/bin/activate  # Для Linux/Mac
   myenv\Scripts\activate     # Для Windows
   
3. **Убедитесь, что у вас установлены все зависимости:**
    ```bash 
   pip install -r requirements.txt

4. **Команда для запуска контейнера Docker и при необходимости сборки всех образов:** 
   ```bash 
   docker compose up --build -d

5. **Откройте новый терминал и создайте суперпользователя для авторизации в админ панеле**
    ```
   docker compose exec web python manage.py createsuperuser

6. **Получение доступа к приложению, запущенному в контейнере, с помощью веб-браузера по ссылке:** http://localhost:8000/admin