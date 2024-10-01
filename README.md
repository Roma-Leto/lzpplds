<h1 style="text-align: center">Dating App</h1>
<h2 style="text-align: center">Пример проекта для Django. Cайт знакомств.</h2>
 
### Функции:
- Регистрация пользователя
- Чат между пользователями один-на-один
- Поиск пользователей по фильтрам
 -----

### Старт
Установить зависимости pip:
```bash
pip install -r requirement.txt
```
Создать секретный ключ.
```bash
python manage.py shell
```
```bash
from django.core.management import utils
utils.get_random_secret_key()
```

Создать файл переменных окружения со сгенерированным ключом.
```
echo SECRET_KEY="_)n5d2_5)u&+wpdd2=_5iz%$jh_3w+v4&#b8t189fbd*r8b^p-">> .env
```
В файле `env` дописать строку `DEBUG=1` для установки режима отладки.

Добавить в settings.py
```python
import os
from dotenv import load_dotenv
load_dotenv()
```

Подготовить базу данных.
```bash
python manage.py migrate
```

Создать суперпользователя.
```bash
python manage.py createsuperuser
```
Запуск сервера отладки проекта.
```bash
python manage.py runserver
```