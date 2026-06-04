"""
Главный скрипт ETL-пайплайна.
Запускает извлечение, очистку и загрузку данных.
"""

from extract import extract
from transform import transform
from load import load

INPUT_FILE = "data/raw_sales.csv"
OUTPUT_FILE = "data/clean_sales.csv"


def main():
    print("=== Запуск ETL-пайплайна ===\n")

    print("1. ИЗВЛЕЧЕНИЕ")
    raw_data = extract(INPUT_FILE)

    print("\n2. ПРЕОБРАЗОВАНИЕ")
    clean_data = transform(raw_data)

    print("\n3. ЗАГРУЗКА")
    load(clean_data, OUTPUT_FILE)

    print(f"\n=== Готово. Результат сохранён в {OUTPUT_FILE} ===")


if __name__ == "__main__":
    main()
