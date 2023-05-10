from bs4 import BeautifulSoup
import requests


data = requests.get('https://rahulshettyacademy.com/AutomationPractice/')
soup = BeautifulSoup(data.content,'html.parser')
# print(soup.prettify())
# if we are running out of attribute then we can directly do this
# Appium is visible text on webpage #all can see
appium=soup.find('a',string='Appium')
print(appium['href'])