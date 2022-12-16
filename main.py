# Importing BeautifulSoup Module
from bs4 import BeautifulSoup
# Importing Request Module
import requests
# Importing lxml Module
import lxml
# Getting the website URL
url=input("Please enter your URL: ")
# Get Requests Website Url
WebReq=requests.get(url)
# Get Web Page Soure from WebReq
WebSource=WebReq.content
# Parse The HTML Source using BeautifulSoup
HTMLSoup=BeautifulSoup(WebSource, features="html5lib")
# Get Anchor Tags from WebSource using BeautifulSoup
Anchor=HTMLSoup.find_all("a")
# Get "href" links without "#"
for links in Anchor:
 if links.get("href")!="#":
  GetLinks=links.get("href")
  if GetLinks[0:8]=="https://":
   print(GetLinks)




# link=input("Enter the link: ")
# text=link[0:26]
# print(text)