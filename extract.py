"""
Извлечение данных из CSV-файла.
Первый этап ETL-пайплайна.
"""

import csv
import os


def extract(filepath):
    """
    Читает CSV-файл и возвращает список словарей.
    Каждый словарь — одна строка файла.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Файл не найден: {filepath}")

    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    if not rows:
        raise ValueError("Файл пуст или содержит только заголовок")

    print(f"[EXTRACT] Прочитано строк: {len(rows)}")
    return rows
