# Перше завдання ----------------------------------------
import datetime

now = datetime.datetime.now()

def get_days_from_today(date):
  diference = now.date().toordinal() - date.toordinal()
  return diference
  
print(get_days_from_today(datetime.date(2028, 9, 24)))
print(get_days_from_today(datetime.date(1996, 9, 24)))

# Друге завдання ------------------------------------------
import random

def get_numbers_ticket(min, max, quantity):
  lottery_numbers = []

  for _ in range(quantity):
    lottery_numbers.append(random.randint(min, max))

  return lottery_numbers

print(f"Ваші лотерейні числа: {get_numbers_ticket(1, 49, 6)}")


# Третє завдання ------------------------------------------
import re

def normalize_phone(phone_number: str) -> str:
  phone_number = phone_number.strip().replace(" ", "") # видаляэмо всі пробіли




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
