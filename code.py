from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/neels/Downloads/chromedriver_win32/chromedriver")
browser.get(starturl)
time.sleep(10)
def scrape():
    headers = ["V Mag","Proper name","Bayer designation","Distance","Spectral class","Mass","Radius","Luminosity"]
    stardata = []
    for i in range(0,98):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for trtag in soup.find_all("ul",attrs={"class","wikipedia"}):
            tdtag = trtag.find_all("li")
            templist = []
            for index,td_tag in enumerate(tdtag):
                if index == 0:
                    templist.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(td_tag.contents[0])
                    except:
                        templist.append("")
            stardata.append(templist)
    print(stardata)
    with open("star.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stardata)
scrape()