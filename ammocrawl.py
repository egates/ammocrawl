import requests
from bs4 import BeautifulSoup

def crawl(url):
    # Send a GET request to the website
    response = requests.get(url)
    if response.status_code == 200:
         print('Success connecting to URL')
    elif response.status_code == 404:
         print('Not Found.')
    # print(response.content)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
    #    print(response.headers)
        # Find all the elements on the page that contain the prices
        price_elements = soup.find_all('span', {'class': 'price'})
        # print(price_elements)
        # Extract the text from each element and convert it to a float
        prices = [float(price_element.text.strip().replace('$', '')) for price_element in price_elements]
        print(prices)
        prices.remove(0.00)
        # Find the minimum price
        min_price = min(prices) if prices else None
        return min_price
    else:
        return None

# Define the URL of the website to be crawled
#url = 'https://www.firearmsdepot.com/ammunition'
url = 'https://www.luckygunner.com/handgun/9mm-ammo'
# Crawl the website
min_price = crawl(url)
# Print the minimum price
print('The minimum price is:', min_price)

#This code uses the requests library to send a GET request to the website, and the BeautifulSoup library to parse the HTML content of the page. The crawl function takes a URL as an input, sends a GET request to the website, parses the HTML content, finds all the elements on the page that contain the prices, extracts the text from each element, converts it to a float, finds the minimum price, and returns it. The code then defines the URL of the website to be crawled, calls the crawl function, and prints the minimum price.

#This is just a simple example, and you may need to modify the code depending on the structure of the websites you want to crawl. The find_all method of the BeautifulSoup object can be used to search for elements on the page based on different criteria, such as class name or tag name.
