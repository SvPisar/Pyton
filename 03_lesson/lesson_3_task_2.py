from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Redmi 12",  "+79247770111"),
    Smartphone("Huawei", "Pura 70", "+79149059152"),
    Smartphone("Honor", "400 Lite", "+79607778802"),
    Smartphone("Ozon",  "i15 ProMAX", "+78919845564"),
    Smartphone("Realme", "GT Neo 6", "+79167899007")
]

for smartphone in catalog:
    print(f"{smartphone.brend} - {smartphone.model}. {smartphone.number}")
