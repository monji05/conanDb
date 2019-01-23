import urllib.request
from bs4 import BeautifulSoup
import requests
import pandas as pd

#no.1-293caseTitle
for i in range(1, 100):
    file_number = "https://websunday.net/conandb/lib/00/{0:04d}.html".format(i)
    html = urllib.request.urlopen(file_number)
    soup = BeautifulSoup(html, "html.parser")
    #title = soup.find("title")
    case = soup.tr.find("p")
    #with open("caseTitle.csv", "a") as f:
    #   f.write("{}{}".format(title.text, "\n"))
    with open("case.csv", "a") as f:
        f.write("{}{}".format(case.text, "\n"))

for i in range(100, 200):
    file_number = "https://websunday.net/conandb/lib/01/{0:04d}.html".format(i)
    html = urllib.request.urlopen(file_number)
    soup = BeautifulSoup(html, "html.parser")
    #title = soup.find("title")
    case = soup.tr.find("p")
    #with open("caseTitle.csv", "a") as f:
    #   f.write("{}{}".format(title.text, "\n")
    with open("case.csv", "a") as f:
        f.write("{}{}".format(case.text, "\n"))

for i in range(200, 294):
    file_number = "https://websunday.net/conandb/lib/02/{0:04d}.html".format(i)
    html = urllib.request.urlopen(file_number)
    soup = BeautifulSoup(html, "html.parser")
    #title = soup.find("title")
    case = soup.tr.find("p")
    #with open("caseTitle.csv", "a") as f:
    #    f.write("{}{}".format(title.text, "\n"))
    with open("case.csv", "a") as f:
        f.write("{}{}".format(case.text, "\n"))

df = pd.read_csv("caseTitle.csv", header=None)
df.to_csv("caseTitle.csv", header=None, index=None)
