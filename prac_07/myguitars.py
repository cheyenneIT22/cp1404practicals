"""CP1404/CP5632 Practical- 07
Guitars program """
from prac_07.guitar import Guitar

file_in = open("guitars.csv", 'r')
guitars = []
for line in file_in:
    line = line.strip()
    parts = line.split(",")
    print(parts)
    print(part for part in parts)
    guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
    name = parts[0]
    year = int(parts[1])
    cost = float(parts[2])
    guitars.append(Guitar(name, year, cost))
    guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
[print(guitar) for guitar in guitars]
