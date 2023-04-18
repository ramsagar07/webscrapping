import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://github.com/collections"
base_url = "http://github.com"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
data1 = soup.find_all("div", class_="col-10 col-md-11")
titles = []
links = []
descriptions = []
for i in data1:
    title = i.find("a").text
    link = base_url + i.find("a")["href"]
    description = i.text.split("\n")
    desc = description[2].strip()
    titles.append(title)
    links.append(link)
    descriptions.append(desc)
dictionary = {"Title" : titles ,
              "Link" : links ,
              "Descriptions" :descriptions}
dataframe = pd.DataFrame(dictionary)
dataframe.to_csv(f"C:\\Users\\i-ray\\PycharmProjects\\web scrapping\\githubdata\\github.csv")
def details(sub_url):
        page1 = requests.get(sub_url)
        soup1 = BeautifulSoup(page1.content, "html.parser")
        data2 = soup1.find_all("article", class_="height-full border color-border-muted rounded-2 p-3 p-md-5 my-5")
        page2_dict = {"Title": [],
                      "Description": [],
                      "Link": [],
                      "stars": []
                      }
        for k in data2:
            title1 = k.find("a").text.strip("\n").split("/")
            if (len(title1)>1):
                sub_title = title1[0].strip("\n")
                if (k.find("div", class_="color-fg-muted mb-2 ws-normal") != None):
                    sub_desc = k.find("div", class_="color-fg-muted mb-2 ws-normal").text
                sub_link = base_url+k.find("a")["href"]
                stars = k.find_all("a")
                star = stars[1].text.strip()
                page2_dict['Title'].append(sub_title)
                page2_dict['Description'].append(sub_desc)
                page2_dict['Link'].append(sub_link)
                page2_dict['stars'].append(star)
                dataframe1 = pd.DataFrame(page2_dict)
                name = sub_title+".csv"
                dataframe1.to_csv(f"C:\\Users\\i-ray\\PycharmProjects\\web scrapping\\githubdata\\{name}", index=False)
                print("parsed  "+name)
for j in links:
    details(j)
