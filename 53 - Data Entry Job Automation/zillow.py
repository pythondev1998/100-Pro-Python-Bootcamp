import requests
from bs4 import BeautifulSoup

class ZillowScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Defined",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,km;q=0.5,zh-TW;q=0.4",
        }
        self.addresses = []
        self.prices = []
        self.urls = []

    def scrape_data(self):
        response = requests.get(self.url, headers=self.headers)
        website_html = response.text
        soup = BeautifulSoup(website_html, "html.parser")

        addresses = soup.find_all('address', {'data-test': 'property-card-addr'})
        prices = soup.find_all('span', {'data-test': 'property-card-price'})
        links = soup.find_all('a', {'data-test': 'property-card-link'})

        base_url = "https://www.zillow.com"
        self.addresses = [address.text.strip() for address in addresses]
        self.prices = [price.text.strip() for price in prices]

        self.urls = []
        for link in links:
            url = base_url + link['href']
            self.urls.append(url)

        data = {
            'prices': self.prices,
            'addresses': self.addresses,
            'urls': self.urls
        }

        return data


