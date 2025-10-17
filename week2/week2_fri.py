import requests
from bs4 import BeautifulSoup
import csv 

try:

    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    response.raise_for_status()
    print("msg is:", response)
    
except Exception as e:
    print("Error during data fetching :" ,e)
        

soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all('div', class_='quote')

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote" ," - ", "Author"]) 

    for i in quotes:
        text = i.find("span", class_="text").get_text()
        author = i.find("small", class_="author").get_text()

        writer.writerow([text , author])
        str  = "..........................................."
        writer.writerow([str])

print("All quotes saved!!!")
