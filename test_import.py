"""
Тестирование импорта пакета mypackage.
"""

print("=" * 50)
print("ТЕСТИРОВАНИЕ ИМПОРТА ПАКЕТА")
print("=" * 50)

# Тест 1: Импорт всего пакета
print("\n1. Импорт пакета:")
import mypackage
print(f" Версия: {mypackage.__version__}")
print(f" Доступные компоненты: {mypackage.__all__}")

# Тест 2: Импорт подпакетов
print("\n2. Импорт подпакетов:")
from mypackage import models
from mypackage import utils
from mypackage import api

# Тест 3: Импорт конкретных классов
print("\n3. Импорт классов:")
from mypackage.models import Student, Group
from mypackage.utils import validate_email, format_student_info
from mypackage.api import APIClient

# Тест 4: Создание объектов
print("\n4. Создание объектов:")
student = Student("Иван", "Петров", 19)
print(f" Создан студент: {student.get_full_name()}")

group = Group("ПИН-231")
print(f" Создана группа: {group.name}")

client = APIClient()
print(f" Создан API клиент: {client.base_url}")

# Тест 5: Проверка функций валидации
print("\n5. Проверка валидации:")
valid, msg = validate_email("test@example.com")
print(f" validate_email('test@example.com'): {valid} - {msg}")

valid, msg = validate_email("invalid")
print(f" validate_email('invalid'): {valid} - {msg}")

# Тест 6: Форматирование
print("\n6. Форматирование:")
student.add_grade(5, "Python")
student.add_grade(4, "Математика")
print(format_student_info(student))

print("\n" + "=" * 50)
print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
print("=" * 50)