"""
Модуль validators - функции для валидации данных.
"""

import re


def validate_email(email):
    """
    Проверяет корректность email адреса.

    Args:
        email (str): Email для проверки

    Returns:
        tuple: (is_valid, error_message)
    """
    if not email:
        return False, "Email не может быть пустым"

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, "Email корректен"
    else:
        return False, "Некорректный формат email"


def validate_age(age):
    """
    Проверяет корректность возраста.

    Args:
        age: Возраст для проверки

    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(age, (int, float)):
        return False, "Возраст должен быть числом"
    if age < 16:
        return False, "Студент должен быть старше 16 лет"
    if age > 100:
        return False, "Некорректный возраст"
    return True, "Возраст корректен"


def validate_grade(grade):
    """
    Проверяет корректность оценки.

    Args:
        grade: Оценка для проверки

    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(grade, (int, float)):
        return False, "Оценка должна быть числом"
    if grade < 2 or grade > 5:
        return False, "Оценка должна быть от 2 до 5"
    return True, "Оценка корректна"


def validate_name(name):
    """
    Проверяет корректность имени/фамилии.

    Args:
        name (str): Имя для проверки

    Returns:
        tuple: (is_valid, error_message)
    """
    if not name or not isinstance(name, str):
        return False, "Имя не может быть пустым"
    if len(name) < 2:
        return False, "Имя должно содержать минимум 2 символа"
    if not name.replace('-', '').replace(' ', '').isalpha():
        return False, "Имя должно содержать только буквы"
    return True, "Имя корректно"

def validate_student_name(first_name, last_name):
    """
    Проверяет имя и фамилию студента.
    Возвращает tuple (is_valid, error_message).
    """
    if not first_name or not last_name:
        return False, "Имя и фамилия не могут быть пустыми"
    if not first_name[0].isupper() or not last_name[0].isupper():
        return False, "Имя и фамилия должны начинаться с заглавной буквы"
    # Разрешены буквы и дефис
    if not all(c.isalpha() or c == '-' for c in first_name) or not all(c.isalpha() or c == '-' for c in last_name):
        return False, "Имя и фамилия могут содержать только буквы и дефис"
    return True, "Имя и фамилия корректны"


# Тестирование валидаторов
if __name__ == "__main__":
    test_emails = ["test@example.com", "invalid-email", "user@domain", "a@b.c"]
    for email in test_emails:
        valid, msg = validate_email(email)
        print(f"{email}: {msg}")