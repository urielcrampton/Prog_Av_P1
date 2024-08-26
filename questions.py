import csv
from typing import List, Tuple

def read_csv(file: str) -> List[Tuple[str, str, str, str]]:
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [(row[0], row[1], row[2], row[3]) for row in reader]