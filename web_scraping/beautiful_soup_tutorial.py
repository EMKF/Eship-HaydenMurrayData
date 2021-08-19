from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

def one_practice():
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    # uses beautiful soup to parse the html from the webpage
    soup = BeautifulSoup(html, "html.parser")

    # use the .get_text() method to remove all of the html tags and replace to remove newline characters
    print(soup.get_text().replace("\n\n", "\n"))

    # use find_all to identify the URLs for all the images on a webpage
    print(soup.find_all("img"))

    # unpack the "img" tags from the list
    image1, image2 = soup.find_all("img")
    print(image1)
    print(image1['src'])
    print(image2)
    print(image2['src'])

    # use .title to access the title and then use .string to clean it up
    print(soup.title.string)

def one_test():
    print("nice")

if __name__ == '__main__':
    # one_practice()
    one_test()

sys.exit()