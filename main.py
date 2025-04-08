# Перше завдання ----------------------------------------
from datetime import datetime

def get_days_from_today(date: str):
  try:
    now = datetime.today().date()
    datetime_object = datetime.strptime(date, "%Y-%m-%d").date()
    difference = now - datetime_object
    return difference.days
   
  except ValueError:
    print(f"Отримано невірний формат дати {date}, правильний: 'РРРР-ММ-ДД'.")

print(get_days_from_today("2020-10-09"))
print(get_days_from_today("09.10.2020"))

# Друге завдання ------------------------------------------
import random

def get_numbers_ticket(min: int, max: int, quantity: int):
  lottery_numbers = []

  for _ in range(quantity):
    lottery_numbers.append(random.randint(min, max))

  return lottery_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа: {lottery_numbers}")


# Третє завдання ------------------------------------------
import re

def normalize_phone(phone_number: str) -> str:
  phone_number = phone_number.strip().replace(" ", "") # видаляэмо всі пробіли
  if phone_number.isdigit() == False:
    pattern = r'[^\d+]'
    phone_number = re.sub(pattern, '', phone_number) # видаляэмо все крім чисел та +
  
  if phone_number.startswith('0') and len(phone_number) == 10:
    phone_number = '38' + phone_number
  
  if phone_number.startswith('38'):
    phone_number = '+' + phone_number

  return phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
