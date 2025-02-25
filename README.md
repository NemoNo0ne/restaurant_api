# Restaurant API (Тестовое задание UTF.tech)

## Описание
API для управления меню ресторана.  
Позволяет получать список категорий блюд с фильтрацией только опубликованных позиций.

## Стек технологий
- Python 3.9
- Django + DRF
- SQLite
- Django ORM

## Установка

### 1. Клонирование репозитория
```sh
git clone https://github.com/nemono0ne/restaurant_api.git
cd restaurant_api
```

### Активация venv и установка зависимостей
```
source .venv/bin/activate  # (Linux/macOS)
```
```
.venv\Scripts\activate  # (Windows)
```
```
pip install -r requirements.txt
```

3. Применение миграций и запуск сервера

```python manage.py migrate```
```python manage.py runserver```

4. Получение списка категорий с блюдами
```http://127.0.0.1:8000/api/v1/foods/```
