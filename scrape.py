from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

headers = ["name", "distance", "mass","radius"]

def scrape(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []

        for table in soup.find_all("table"):
            tr_tags = table.find_all("tr")
            
            for tr_tag in tr_tags:
                try:
                    td = tr_tag.find_all("td")
                    row = [i.text.rstrip() for i in td]
                    temp_list.append(row)
                except:
                    temp_list.append("")
    except:
        time.sleep(1)
        scrape(hyperlink)

    
    Star_names = []
    Distance =[]
    Mass = []
    Radius =[]
    
    for i in range(1,len(temp_list)):

        Star_names.append(temp_list[i][1])
        Distance.append(temp_list[i][3])
        Mass.append(temp_list[i][5])
        Radius.append(temp_list[i][6])
    
    df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=headers)

    df2.to_csv('bright_stars.csv')

scrape(START_URL)
