import requests
from bs4 import BeautifulSoup
import pandas as pd
book_name= []
book_price = []
availability = []
for i in range(1, 51, 1):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    page =requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find_all("article", class_="product_pod")
    for j in data:
        name = j.find("img")
        title = name .attrs["alt"]
        pricing = j.find("p", class_="price_color").text
        stock = j.find("p", class_="instock availability").text.strip()
        book_name.append(title)
        book_price.append(pricing)
        availability.append(stock)

data1 = {"Name": book_name,
         "Price": pricing,
         "Availability": availability
         }
dataframe = pd.DataFrame(data1)
dataframe.to_csv("Books.csv", index=False)
