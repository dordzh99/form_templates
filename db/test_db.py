from tinydb import TinyDB

db = TinyDB("db/form_templates.json")

templates = [
    {
        "name": "MyForm",
        "user_name": "text",
        "my_date": "date",
        "lead_email": "email"
    },
    {
        "name": "MyCustomForm",
        "user_name": "text",
        "my_date": "date",
        "lead_email": "email",
        "my_phone": "phone"
    },
    {
        "name": "OrderForm",
        "customer_name": "text",
        "order_date": "date",
        "phone_number": "phone"
    },
    {
        "name": "RegistrationForm",
        "login": "text",
        "password": "text",
        "birth_date": "date",
        "mobile_phone": "phone"
    }
]

db.insert_multiple(templates)
