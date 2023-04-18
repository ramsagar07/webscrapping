import requests
from bs4 import BeautifulSoup
from csv import writer
with open("IMBD1000.csv", "w", newline='') as f:
    writerr = writer(f)
    header = ["Rank", "Title", "Year", "Rating", "Director", "Rating"]
    writerr.writerow(header)
    for i in range(1, 1000, 100):
        url = "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start="+str(i)+"&ref_=adv_nxt"
        page = requests.get(url)
        parse = BeautifulSoup(page.content, "html.parser")
        data = parse.find_all("div", class_="lister-item-content")
        print(f"parsing page {i}")
        for j in data:
            rank = j.find("span", class_="lister-item-index unbold text-primary").text.strip(".")
            a_tag = j.find_all("a")
            name = a_tag[0].text
            year = j.find("span", class_="lister-item-year text-muted unbold").text.strip("()")
            rating = j.find("div", class_="inline-block ratings-imdb-rating").text.strip()
            dire = j.find_all("p")
            direc = dire[2]
            director = direc.find("a").text
            collection = j.find_all("span", attrs={"name": "nv"})
            if len(collection)>1:
                collect = collection[1].text
            else:
                collect = "not mentioned"

            data1 = [rank, name, year, rating, director, collect]
            writerr.writerow(data1)
