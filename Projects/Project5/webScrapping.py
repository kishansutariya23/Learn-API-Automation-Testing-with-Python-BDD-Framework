# No need to rely on front end part like selenium to extract the data
# with help of this package we can do it in seconds


from bs4 import BeautifulSoup
import requests

# data = requests.get('https://www.imdb.com/find/?s=ep&q=thriller&ref_=nv_sr_sm')
# data = requests.get('https://www.amazon.com')
# data = requests.get('https://www.rahulshettyacademy.com/seleniumPractise/#/')
# above have JS so it some tough to automate as they will hide html


# use below which has only html and it will be easy to automate
data = requests.get('https://rahulshettyacademy.com/AutomationPractice/')
soup = BeautifulSoup(data.content,'html.parser')
# print(soup.prettify())
# above we use html.parser  so it will show o/p in terminal same as in developer o/p of browser
# html code for the website

table = soup.find('table',{'class':'table-display'}) # tag and attribute are passed
# print(table.prettify())
rows = table.findAll('tr')
# NOW WE WILL PRINT THE COURSE NAMES
for row in rows:
    # print(row)
    rowdata = row.findAll('td')
    # if we have more drop down like inside td we have a then we can use .a or .find
    if len(rowdata) ==0:
        print('-----empty-----')
    else:
        # print(rowdata[1].a.text)
        print(rowdata[1].text)
    # print(rowdata)
# think that all course name are links to new page and there is price to that course in new page
#         subUrl = rowdata[1].a['href']
#         subData = requests.get("https://rahulshettyacademy.com/"+subUrl)
#         childSoup = BeautifulSoup(subData.content, 'html.parser')
#         inspect the new page and find the price
#         price = childSoup.find('div',{'class':'----'})
        # we got price-div and then we are searching for text/number of that price
        # print(price.a.text)

# you can write the condition "if" as some time we dont have any content and script stop
# if condition is true then enter inside and run next statement and append all the course in list and print final o/p
# we can write condition that price >400 should be appended in list ....

# --------------------------------------------

