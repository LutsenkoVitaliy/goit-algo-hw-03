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

def normalize_phone(phone_number):
  pass