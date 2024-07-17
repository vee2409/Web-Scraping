!pip install requests beautifulsoup4 pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://hprera.nic.in/PublicDashboard"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())
project_links = []
tables = soup.find_all('table')


for table in tables:
    if 'Registered Projects' in table.get_text():
        rows = table.find_all('tr')[1:7]  # Skip the header row and take the first 6 projects
        for row in rows:
            link = row.find('a', href=True)
            if link:
                project_links.append("https://hprera.nic.in" + link['href'])
        break

print(project_links)
!pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://hprera.nic.in/PublicDashboard"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')


print(soup.prettify())


project_links = []
tables = soup.find_all('table')


for table in tables:
    if 'Registered Projects' in table.get_text():
        rows = table.find_all('tr')[1:7]  # Skip the header row and take the first 6 projects
        for row in rows:
            link = row.find('a', href=True)
            if link:
                project_links.append("https://hprera.nic.in" + link['href'])
        break

print(project_links)


def get_project_details(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')

    details = {}
    try:
        details_table = soup.find('table', class_='table')  # Adjust the class or find logic if necessary
        rows = details_table.find_all('tr')

        for row in rows:
            columns = row.find_all('td')
            if len(columns) == 2:
                key = columns[0].get_text(strip=True)
                value = columns[1].get_text(strip=True)
                if key in ['GSTIN No', 'PAN No', 'Name', 'Permanent Address']:
                    details[key] = value
    except Exception as e:
        print(f"Error parsing {url}: {e}")
    
    return details


projects = []

for link in project_links:
    project_details = get_project_details(link)
    projects.append(project_details)


df = pd.DataFrame(projects)
print(df)
