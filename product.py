import requests
from bs4 import BeautifulSoup

def get_product_links(url):
    product_links = []
    page_number = 1

    while True:
        page_url = f"{url}?page={page_number}"
        response = requests.get(page_url)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('a', class_='product-link')

        if not products:
            break

        for product in products:
            product_links.append(product['href'])

        page_number += 1

    return product_links

url = "https://www.zap.co.il/models.aspx?sog=e-cellphone"
product_links = get_product_links(url)
print(product_links)
