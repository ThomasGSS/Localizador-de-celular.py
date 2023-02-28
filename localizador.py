## https://pypi.org/project/phonenumbers/ salvando o link aqui para caso de algum problema no codigo##


import phonenumbers

from phonenumbers import geocoder

Number= str(input("digite o numero:"))

ch_number= phonenumbers.parse(Number, "CH")
print('')
print('local:', geocoder.description_for_number(ch_number,"en"))
print("")
from phonenumbers import carrier
service_number = phonenumbers.parse(Number, "RO")
print('Operadora Do Celular:', carrier.name_for_number(service_number,"en"))
