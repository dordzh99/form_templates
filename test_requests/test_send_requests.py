import httpx

url = "http://127.0.0.1:8000/get_form"

data1 = {
    "user_name": "dordzhi",
    "my_date": "2023-11-16",
    "lead_email": "dor@mail.ru"
}

data2 = {
    "user_name": "dordzhi",
    "my_date": "2023-11-16",
    "lead_email": "dor@mail.ru",
    "my_phone": "+79374661212"
}

data3 = {
    "login": "dordzhi",
    "password": "dordzhi",
    "birth_date": "22.02.2022"
}

data4 = {
    "customer_name": "dordzhi",
    "order_date": "22.022022",
    "phone_number": "+7 925 255 25 25"
}

response1 = httpx.post(url, json=data1)
response2 = httpx.post(url, json=data2)
response3 = httpx.post(url, json=data3)
response4 = httpx.post(url, json=data4)

print(response1.json())
print(response2.json())
print(response3.json())
print(response4.json())
