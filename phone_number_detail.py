import phonenumbers
from phonenumbers import timezone, geocoder,carrier

numbers = input('Enter you no with urzone code +__:')
phone=phonenumbers.parse(numbers)
time =timezone.time_zones_for_number(phone)
carr = carrier.name_for_number(phone,'en')
reg =geocoder.description_for_number(phone,'en')
print(phone)
print(time)
print(carr)
print(reg)
