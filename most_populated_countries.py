from bs4 import BeautifulSoup
import requests

# VARS
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
countries_file = "countries.txt"


# CAPITALIZE STRING
def capitalize(string):
    return string[1].upper() + string[2:]


# FETCH LIST OF COUNTRIES FROM FILE
def get_all_countries():
    with open(countries_file, "r") as f:
        all_lines = f.readlines()

    countries = []
    for line in all_lines:
        line = line.strip("\r").strip("\n")
        line = line.lower()
        if len(line) >= 2:
            countries.append(line)
    return countries


# FETCH AND PARSE
def display_population_data(URL=url, delimeter='->'):
    html = requests.get(URL)
    soup = BeautifulSoup(html.content, "html.parser")

    all_data = soup.find_all("td")

    # GET A LIST OF ALL COUNTRIES
    valid_countries = get_all_countries()

    i = 0
    while i < len(all_data):
        data = all_data[i].text.lower()
        try:
            for country in valid_countries:
                if country in data:
                    country_name = data
                    population = all_data[i + 1].text
                    if "," in population:
                        print(country_name[1:].title(), delimeter, population)
                    i += 1
                    continue

            i += 1
        except:
            continue


display_population_data()
