# Перше завдання
import datetime

now = datetime.datetime.now()

def get_days_from_today(date):
  diference = now.date().toordinal() - date.toordinal()
  return diference
  
#print(get_days_from_today(datetime.date(2028, 9, 24)))
#print(get_days_from_today(datetime.date(1996, 9, 24)))

# Друге завдання
import random

def get_numbers_ticket(min, max, quantity):
  #lottery_numbers = random.randint(min, max)

  for lottery_numbers in range(quantity):
    pass
    # print(random.randint(min, max))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа: {lottery_numbers}")


print("fdsfsdf")