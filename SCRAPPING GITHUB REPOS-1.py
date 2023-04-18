import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
links = []
topic = []
base_url = "http://github.com"


def get_topics(github_url):
    page = requests.get(github_url)
    data = BeautifulSoup(page.content, "html.parser")
    data1 = data.find_all("div", class_="py-4 border-bottom d-flex flex-justify-between")
    description =[]
    for name in data1:
        topics = name.find("p", class_="f3 lh-condensed mb-0 mt-1 Link--primary").text
        topics_description = name.find("p", class_="f5 color-fg-muted mb-0 mt-1").text.strip()
        link = base_url+name.find('a')['href']
        topic.append(topics)
        description.append(topics_description)
        links.append(link)
    dict1 = {"Topic": topic,
             "Description": description,
             "Links": links}
    dataframe = pd.DataFrame(dict1)
    dataframe.to_csv("Topics.csv")


url = "https://github.com/topics"
get_topics(url)


def get_sub_topics(sub_url):
    page1 = requests.get(sub_url)
    soup = BeautifulSoup(page1.content, "html.parser")
    repo_tag = soup.find_all("h3", class_="f3 color-fg-muted text-normal lh-condensed")
    # a_tag = repo_tag[0].find_all("a")
    star_tag = soup.find_all("span", id="repo-stars-counter-star")

    def convert(stars):

        if stars[-1] =='k':
            return int(float(stars[:-1])*1000)
        return int(stars[:-1])

    def repo_info(h1_tag, star_tags):
        a_tags = h1_tag.find_all("a")
        user = a_tags[0].text.strip()
        repo = a_tags[1].text.strip()
        repo_url = base_url+a_tags[1]["href"]
        stars = convert(star_tags.text.strip())
        return user, repo, repo_url, stars

    page2_dict = {"user": [],
                  "repository": [],
                  "repository_url": [],
                  "stars": []

                  }
    for j in range(len(repo_tag)):
        output = repo_info(repo_tag[j], star_tag[j])
        page2_dict['user'].append(output[0])
        page2_dict["repository"].append(output[1])
        page2_dict["repository_url"].append(output[2])
        page2_dict["stars"].append(output[3])
    os.makedirs("data", exist_ok=True)
    name = topic[i] + ".csv"
    page2_dataframe = pd.DataFrame(page2_dict)
    page2_dataframe.to_csv(f"C:\\Users\\i-ray\\PycharmProjects\\web scrapping\\data\\{name}")
    print("scrapped "+name)


for i in range(len(links)):
    topic_url = links[i]
    get_sub_topics(topic_url)
