import re
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "http://mfd.ru/currency/?currency=USD"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find_all("table", {"class": "mfd-currency-table"})[0]
rows = table.find_all('tr')

x = []
y = []


for i in range(40, 0, -1):
    cells = rows[i].find_all('td')
    if len(cells) > 0:
        x.append(cells[0].text.strip()[1:])
        y_value = re.sub(r'[^\d.]', '', cells[1].text.strip()).replace(',', '.')
        y.append(float(y_value))

plt.plot(x, y)
plt.xlabel('Дни')
plt.ylabel('Курс')
plt.title('График курса USD')
plt.xticks(rotation=80)
plt.tight_layout() 
plt.show()