#made by amir_bou
import  phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
ch_number = phonenumbers.parse(input('what is the number: '))
print(geocoder.description_for_number(ch_number,"en"))
print(carrier.name_for_number(ch_number, "en"))