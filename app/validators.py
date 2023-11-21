import re

from fastapi import HTTPException

def validate_field(value, field_type):
    if field_type == "date" and not validate_date(value):
        raise HTTPException(status_code=422, detail=f"Неправильно введена дата!")
    elif field_type == "phone" and not validate_phone(value):
        raise HTTPException(status_code=422, detail=f"Неправильно введен номер телефона!")
    elif field_type == "email" and not validate_email(value):
        raise HTTPException(status_code=422, detail=f"Неправильно введен email!")
    return True

def determine_field_type(value):
    if validate_date(value):
        return "date"
    elif validate_phone(value):
        return "phone"
    elif validate_email(value):
        return "email"
    else:
        return "text"

def validate_date(value):
    samples = [
        re.compile(r'^\d{2}\.\d{2}\.\d{4}$'),
        re.compile(r'^\d{4}\-\d{2}\-\d{2}$')
    ]
    return any(sample.match(value) for sample in samples)

def validate_phone(value):
    sample = re.compile(r'\+7\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2}$')
    return bool(sample.match(value))

def validate_email(value):
    sample = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(sample.match(value))
