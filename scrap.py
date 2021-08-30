# if you want to scrape a website
# 1. Use the API
# 2.   HTML Web Scrapping using some tool like bs4

# by using this module 

# pip install requests
# pip install bs4
# pip install html5lib


import requests
from bs4 import BeautifulSoup
url = "https://code2hell.herokuapp.com/"


# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
print(htmlContent)


# Step 2: parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)


# Step 3: HTML Tree Traversal ->(Commonly used type of objects)
# 3.1 Tag

title = soup.title
print(title)
# 3.2 NavigableString
print(type(title.string))
# 3.3 BeautifulSoup
print(type(soup))
# 4.4 Comment
markup = "<p><!--this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)
print(soup2.p.string)
# exit()  



# *******Started Scriptin each element of the HTML*****


# get the title of the pragraphs of the html page
paras = soup.find_all('p')
# print(paras)

# get the classes of any  element of the html page
print(soup.find('p')['class'])

# find all the element with class lead of the html page
print(soup.find_all("p", class_= "lead"))
print(soup.find('p').get_text())
print(soup.get_text())



# get the title of the AnchorTags of the html page
anchors = soup.find_all('a')
# print(anchors)


# printing all link of the website
all_links = set() 
for link in anchors: 
    # print(link.get("href"))
    if(link.get("href") != '#'):
        linkText = ("https://code2hell.herokuapp.com/" +link.get('href'))
        all_links.add(link)
        print(linkText)


