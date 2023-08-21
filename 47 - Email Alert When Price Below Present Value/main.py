import requests, smtplib
from bs4 import BeautifulSoup

BUY_PRICE = 28

URL = "https://www.amazon.com/-/es/Agua-colonia-Armaf-Tres-hombre/dp/B00NQGPPW8/ref=sr_1_15?keywords=ARMAF&qid=1685395152&sr=8-15"
HEADERS = {
    "User-Agent": "Defined",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,km;q=0.5,zh-TW;q=0.4",
    }

MY_EMAIL = "pythoncodebrian@gmail.com"
MY_PASSWORD = ""
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT= 587


response = requests.get(URL, headers=HEADERS)
website = response.content
     
soup = BeautifulSoup(website, "lxml")
price_tag = soup.find(class_="a-size-medium a-color-price", id="price_inside_buybox")
price = float(price_tag.get_text().split("$")[1].strip())
print(price)


title = soup.find(id="productTitle").get_text().strip()
print(title)


if(price <  BUY_PRICE):
    message = f"{title} is now {price}"
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="brianfortuna95@gmail.com",
                    msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
                )

