import csv
from .paths import ECOMMERCE_FILE

def read_csv(file_path=ECOMMERCE_FILE) :
    #Returnerar hela CSV-filen som list[dict]
    
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, skipinitialspace=True) #Läser första raden som nycklar
        rows = list(reader)
        header = reader.fieldnames
    return header, rows
    # for row in reader:
    #     print(row["city"])
if __name__ == "__main__":
    print("Testar read_csv...\n")

    header, rows = read_csv()
    print("Header:", header)
    print("Antal rader:", len(rows))

    if rows:
        print("\nFörsta rad:")
        print(rows[0])
    else:
        print("Inga rader hittades!")

