import requests
from bs4 import BeautifulSoup
import re
import csv

url = 'https://www.dotabuff.com/heroes?show=facets&view=played&mode=turbo&date=7d'

def scrape_all_heroes(url):
    # Add headers to mimic a real browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        heroes_data = []

        heroes = soup.find_all('tr', class_="tw-border-b tw-transition-colors hover:tw-bg-muted/50 data-[state=selected]:tw-bg-muted")
        # href = heroes.find("a")
        for hero in heroes:
            facets = hero.find("div", {"class":"tw-text-xs tw-text-secondary"})
            a_tag = hero.find('a', class_='tw-flex tw-items-center tw-gap-3')
            numbers = hero.find_all('div', class_='tw-flex tw-w-full tw-flex-col tw-items-start tw-gap-1', limit=5)

            if a_tag:
                href = a_tag['href']

                match = re.search(r'/heroes/(.*)', href)
                if match:
                    hero_name = match.group(1)
                    facet = facets.text
                    
                    if len(numbers) == 5:
                        win_rate = numbers[2]
                        no_matches = numbers[0]
                        kda = numbers[4]

                        heroes_data.append([hero_name, facet, win_rate.text, no_matches.text, kda.text])
                        # print(f'{hero_name}, {facet}, {win_rate.text}, {no_matches.text}, {kda.text}')
        
        return heroes_data
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
        return []
    
def write_to_csv(data, file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Hero Name", "Facet", "Win Rate", "No Matches", "KDA"])
        writer.writerows(data)


heroes_data = scrape_all_heroes(url)

if heroes_data:
    write_to_csv(heroes_data, "heroes_data.csv")
