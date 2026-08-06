from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15 Pro", "+79885545688"),
    Smartphone("Samsung", "Galaxy S24", "+79386698523"),
    Smartphone("Xiaomi", "13T Pro", "+9887413698"),
    Smartphone("Apple", "iPhone 17 Pro Max", "+9184410258"),
    Smartphone("Samsung", "Galaxy Z Fold8 Ultra", "89002586633")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
