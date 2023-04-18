import requests
from bs4 import BeautifulSoup
import openpyxl
import pandas as pd
from csv import writer
with open("IMDB.csv", "w", newline='', encoding="utf8") as f:
    write = writer(f)
    header = ["Rank", "Name", "Year", "Rating"]
    write.writerow(header)
    wrkbook = openpyxl.Workbook()
    sheet = wrkbook.active
    sheet.title = "Top Rated Movies"
    sheet.append(["Rank", "Name", "Year", "Rating"])
    try:
        url = "https://www.imdb.com/chart/top/"
        page = requests.get(url)
        page.raise_for_status()
        data = BeautifulSoup(page.content, "html.parser")
        movies = data.find("tbody", class_="lister-list").find_all("tr")
        for movie in movies:
            rank = movie.find("td", class_="titleColumn").get_text(strip=True)[0]
            name = movie.find("td", class_="titleColumn").a.text
            year = movie.find("span", class_="secondaryInfo").text.strip("()")
            rating = movie.find("td", class_="ratingColumn imdbRating").text.strip()
            sheet.append([rank, name, year, rating])
            data2 = [rank, name, year, rating]
            write.writerow(data2)
        wrkbook.save("movies.xlsx")
    except Exception as e:
        print(e)
    data1 = pd.read_excel("movies.xlsx")
    data1.to_excel("movie.xlsx")
