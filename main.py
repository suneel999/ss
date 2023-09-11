import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("Usage: python main.py <search_query>")
    sys.exit(1)

search_query = sys.argv[1]

product_names = []
product_prices = []
product_descriptions = []

page_number = 1

while True:
    url = f"https://www.flipkart.com/search?q={search_query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page_number}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find all the product names on the page
    names = soup.find_all("div", class_="_4rR01T")
    prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
    descriptions = soup.find_all("div", class_="fMghEO")

    # If no more products are found on the page, break the loop
    if not names:
        break

    # Extract and append the text of each product name, price, and description to respective lists
    for name, price, desc in zip(names, prices, descriptions):
        product_names.append(name.text)
        product_prices.append(price.text)
        product_descriptions.append(desc.text)

    # Move to the next page
    page_number += 1

# Print the collected data
for i, (name, price, desc) in enumerate(zip(product_names, product_prices, product_descriptions), start=1):
    print(f"{i}. Name: {name}")
    print(f"   Price: {price}")
    print(f"   Description: {desc}\n")
