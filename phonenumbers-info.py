import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

phno=phonenumbers.parse("+918106237018")

print("Country: " + geocoder.description_for_number(phno,"en"))
print("Time zone: " + str(timezone.time_zones_for_number(phno)))
print("Carrier: " + carrier.name_for_number(phno,"en"))