import requests
from bs4 import BeautifulSoup
import lxml
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
LANGUAGE = "en-US,en;q=0.9"
url = "https://www.amazon.com/Bose-Sport-Earbuds-Earphones-Headphones/dp/B08CJCTG6Z/ref=sr_1_8?crid=WUIR3GV8E9X3&currency=INR&keywords=boat%2Bairdopes&qid=1661996742&sprefix=boat%2Bairdope%2Caps%2C614&sr=8-8&th=1"
header = {
    "User-Agent": USER_AGENT,
    "Accept-Language":LANGUAGE,
    "Accept-Encoding":"gzip, deflate",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
response = requests.get(url,headers=header)
soup = BeautifulSoup(response.content,"html.parser")
print(soup)
# price = soup.find(id="priceblock_ourprice").get_text()
# price_without_currency = price.split("$")[1]
# price_as_float = float(price_without_currency)
# print(price_as_float)