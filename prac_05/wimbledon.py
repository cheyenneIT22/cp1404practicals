FILE_NAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    records = get_records(FILE_NAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record)[INDEX_COUNTRY]
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return


def display_results(champion_to_count, countries):
    print("Wimbledon Champion: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won wimbledon:  ")
    print(",".join(country for country in sorted(countries)))


def get_records(FILE_NAME):
    records = []
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)


main()
