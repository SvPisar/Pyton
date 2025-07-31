from address import Address
from mailing import Mailing

to_address = Address("109012", "Москва", "Тверская", "1", "9")
from_address = Address("420111", "Казань", "Нагорная", "6", "56")
mailing = Mailing("UNIK8990", to_address, from_address, 1010)
print(mailing)
