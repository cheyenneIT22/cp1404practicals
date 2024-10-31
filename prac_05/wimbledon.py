"""CP1401, Prac05, Wimbledon program to process the data and display processed information."""


def main():
    """Main function to process data from file."""
    file_path = 'wimbledon.csv'  # Modify with your file's path
    champions_data = load_data(file_path)

    champion_counts = count_champions(champions_data)
    countries = get_countries(champions_data)

    # Display results
    display_results(champion_counts, countries)


def load_data(file_path):
    """ Reads the file line by line and splits the data by commas."""
    # Assuming the file contains data in the format: "Year, Champion, Country"
    champions_data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = \
                line.strip()
            if line:
                year, champion, country = line.split(',')
                champions_data.append((champion.strip(), country.strip()))
    return champions_data


def count_champions(champions_data):
    """Iterates through the list of champions and counts how many times each champion has won."""
    # Counts how many times each champion has won
    champion_counts = {}
    for champion, _ in champions_data:
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts


def get_countries(champions_data):
    """Gets the unique countries from data set and sorts alphabetically."""
    countries = sorted(set(country for _, country in champions_data))
    return countries


def display_results(champion_counts, countries):
    """Displays both the champion count and the sorted list of countries."""
    print("Champions and how many times they have won:")
    for champion, count in champion_counts.items():
        print(f"{champion}: {count} times")

    print("\nCountries of the champions in alphabetical order:")
    for country in countries:
        print(country)
