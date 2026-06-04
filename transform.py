"""
Очистка и преобразование данных.
Второй этап ETL-пайплайна.
"""

from datetime import datetime


def parse_date(value):
    """
    Пробует распарсить дату из разных форматов.
    Возвращает строку в формате YYYY-MM-DD или None.
    """
    if not value or not value.strip():
        return None

    value = value.strip()

    formats = [
        "%Y-%m-%d",
        "%d.%m.%Y",
        "%d/%m/%Y",
        "%Y/%m/%d",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return None


def parse_price(value):
    """
    Убирает пробелы из цены и преобразует в число.
    Возвращает float или None.
    """
    if not value or not value.strip():
        return None

    cleaned = value.strip().replace(" ", "").replace(",", ".")

    try:
        return float(cleaned)
    except ValueError:
        return None


def parse_quantity(value):
    """
    Преобразует количество в целое число.
    Возвращает int или None.
    """
    if not value or not value.strip():
        return None

    try:
        return int(value.strip())
    except ValueError:
        return None


def transform(rows):
    """
    Принимает список словарей (из extract.py).
    Удаляет битые строки, чистит поля, добавляет total.
    Возвращает список очищенных словарей.
    """
    cleaned = []
    skipped = 0

    for i, row in enumerate(rows, start=1):
        date = parse_date(row.get("date", ""))
        product = row.get("product", "").strip()
        quantity = parse_quantity(row.get("quantity", ""))
        price = parse_price(row.get("price", ""))

        if not date or not product or quantity is None or price is None:
            print(f"[TRANSFORM] Пропущена строка {i}: неполные данные")
            skipped += 1
            continue

        total = round(quantity * price, 2)

        cleaned.append({
            "date": date,
            "product": product,
            "quantity": quantity,
            "price": price,
            "total": total,
        })

    print(f"[TRANSFORM] Обработано строк: {len(cleaned)}, пропущено: {skipped}")
    return cleaned
