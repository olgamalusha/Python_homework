from address import Address
from mailing import Mailing

to_addr = Address("350000", "Краснодар", "Красная", "10", "15")
from_addr = Address("101000", "Москва", "Тверская", "5", "12")

mailing = Mailing(
    to_address=to_addr, from_address=from_addr, cost=5000, track="IN12345944"
    )

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
