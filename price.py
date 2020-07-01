import requests
import re
from bs4 import BeautifulSoup
import time
import smtplib, ssl

states = {
    'alabama': 'al',
    'alaska': 'ak',
    'american samoa': 'as',
    'arizona': 'az',
    'arkansas': 'ar',
    'california': 'ca',
    'colorado': 'co',
    'connecticut': 'ct',
    'delaware': 'de',
    'district of columbia': 'dc',
    'florida': 'fl',
    'georgia': 'ga',
    'guam': 'gu',
    'hawaii': 'hi',
    'idaho': 'id',
    'illinois': 'il',
    'indiana': 'in',
    'iowa': 'ia',
    'kansas': 'ks',
    'kentucky': 'ky',
    'louisiana': 'la',
    'maine': 'me',
    'maryland': 'md',
    'massachusetts': 'ma',
    'michigan': 'mi',
    'minnesota': 'mn',
    'mississippi': 'ms',
    'missouri': 'mo',
    'montana': 'mt',
    'nebraska': 'ne',
    'nevada': 'nv',
    'new hampshire': 'nh',
    'new jersey': 'nj',
    'new mexico': 'nm',
    'new york': 'ny',
    'north carolina': 'nc',
    'north dakota': 'nd',
    'northern mariana islands':'mp',
    'ohio': 'oh',
    'oklahoma': 'ok',
    'oregon': 'or',
    'pennsylvania': 'pa',
    'puerto rico': 'pr',
    'rhode island': 'ri',
    'south carolina': 'sc',
    'south dakota': 'sd',
    'tennessee': 'tn',
    'texas': 'tx',
    'utah': 'ut',
    'vermont': 'vt',
    'virgin islands': 'vi',
    'virginia': 'va',
    'washington': 'wa',
    'west virginia': 'wv',
    'wisconsin': 'wi',
    'wyoming': 'wy',
}

HEADERS = {"User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15"}
URL = "https://www.nerdwallet.com/cost-of-living-calculator/city-life/"
city = input("what city? ")
city = city.replace(' ', "-")
state = input("what state? ").lower()
abbreviation = str(states[state])
URL = URL + city + "-" + abbreviation
page = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(page.content, 'html.parser')

def get_product_name():
    title = soup.find('h1').get_text().strip()
    return title

#def get_utilities():


#def get_grocery_cost():

def get_median_salary():
    median_salary = soup.find("div",{"class":"cl-results-header-income"}, {"class":"col-results-important"}).get_text().strip()[1:3]
    median_salary2 = soup.find("div",{"class":"cl-results-header-income"}, {"class":"col-results-important"}).get_text().strip()[4:]
    median_salary = int(median_salary) * 1000 + int(median_salary2)
    return median_salary

def get_average_rent():
    monthly_rent = int(soup.find("div",{"class":"cl-results-table-entry"}).nextSibling.get_text().strip(' $').replace(',', ''))
    yearly_rent = monthly_rent * 12
    rent = [monthly_rent, yearly_rent]
    return rent

if __name__ == "__main__":
    print(get_median_salary())