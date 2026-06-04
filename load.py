"""
Сохранение обработанных данных в CSV-файл.
Третий этап ETL-пайплайна.
"""

import csv
import os


def load(rows, output_path):
    """
    Принимает список словарей и сохраняет в CSV.
    Создаёт папку для выходного файла, если её нет.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fieldnames = ["date", "product", "quantity", "price", "total"]

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"[LOAD] Сохранено строк: {len(rows)} в файл {output_path}")
