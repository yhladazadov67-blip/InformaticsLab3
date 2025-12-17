# File: Informatics_Lab3_Task2.py
# Author = Азадов Ыхлас
# Group = 3132
# Date = 12.12.2025

"""
Вариант 0 (ИСУ % 5 = 0).
Проверка корректности email.
Если email корректен — вывести почтовый сервер (часть после '@'),
иначе вывести 'Fail!'.
"""

import re

EMAIL_RE = re.compile(r'^[A-Za-z0-9._]+@([A-Za-z]+(\.[A-Za-z]+)+)$')

def extract_mail_server(email: str) -> str:
    match = EMAIL_RE.fullmatch(email.strip())
    if not match:
        return "Fail!"
    return match.group(1)

# Минимум 5 тестов
TESTS = [
    ("students.spam@yandex.ru", "yandex.ru"),
    ("example@example.com", "example.com"),
    ("example@example", "Fail!"),
    ("user_name123@mail.server.co", "mail.server.co"),
    ("bad@name@domain.com", "Fail!"),
]

if __name__ == "__main__":
    email = input().strip()
    print(extract_mail_server(email))