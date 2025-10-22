import csv
from paths import ECOMMERCE_FILE

with open(ECOMMERCE_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, skipinitialspace=True) #Läser första raden som nycklar
    header = reader.fieldnames

    print(header)
    # for row in reader:
    #     print(row["city"])
