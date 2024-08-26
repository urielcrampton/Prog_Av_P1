import csv
from typing import List, Tuple

def read_csv(file: str) -> List[Tuple[str, str, str, str]]:
    with open(file, newline='', encoding='latin1') as csvfile:  # Usar 'latin1' en lugar de 'utf-8'
        reader = csv.reader(csvfile)
        return [
            (row[0], row[1], row[2], row[3])
            for row in reader
            if len(row) >= 4  # Asegura que la fila tiene al menos 4 elementos
        ]
