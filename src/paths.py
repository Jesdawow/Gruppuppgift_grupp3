from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] #Projektroten ligger en nivå ovanför src-mappen som denna fil ligger i.

#Sökvägar för data-mappen
DATA_DIR = ROOT / "data" #använd för att hitta data-mappen
ECOMMERCE_FILE = DATA_DIR / "ecommerce_sales.csv" #använd för att anropa filen

#Sökvägar för src-mappen
SRC_DIR = ROOT / "src" #sökväg till SRC-mappen
