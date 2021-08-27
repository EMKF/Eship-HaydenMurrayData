from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup
import sys

def one_practice():
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    # uses beautiful soup to parse the html from the webpage
    soup = BeautifulSoup(html, "html.parser")
    print(soup)

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
    """
    Using Beautiful Soup, print out a list of all the links on the page by looking for HTML tags with the name a and
    retrieving the value taken on by the href attribute of each tag build url from base url + relative url
    """
    base_url = "http://olympus.realpython.org"
    html_page = urlopen(base_url + "/profiles")
    html_text = html_page.read().decode("utf-8")
    # uses beautiful soup to parse the html from the webpage
    soup = BeautifulSoup(html_text, "html.parser")
    # inspect it
    print(soup)
    """
    The relative URL for each link can be accessed through the "href" subscript.
    Concatenate this value with base_url (above) to create the full link_url.
    """
    for link in soup.find_all("a"):
        link_url = base_url + link["href"]
        print(link_url)

def mech_soup():
    # use mechanical soup to work with a webpage with forms and buttons to click
    """
    You create a Browser instance and use it to request the URL http://olympus.realpython.org/login.
    You assign the HTML content of the page to the login_html variable using the .soup property.
    """
    browser = mechanicalsoup.Browser()
    url = "http://olympus.realpython.org/login"
    login_page = browser.get(url)
    login_html = login_page.soup

    """
    login_html.select("form") returns a list of all <form> elements on the page. Since the page has only one <form> element,
    you can access the form by retrieving the element at index 0 of the list. The next two lines select the username and 
    password inputs and set their value to "zeus" and "ThunderDude", respectively.
    """
    # Access the username and password form in the login_html
    form = login_html.select("form")[0]
    # assign username
    form.select("input")[0]["value"] = "zeus"
    # assign password
    form.select("input")[1]["value"] = "ThunderDude"

    """
    You submit the form with browser.submit(). Notice that you pass two arguments to this method, 
    the form object and the URL of the login_page, which you access via login_page.url.
    """
    # pass the form (above) through the login page created (above)
    profiles_page = browser.submit(form, login_page.url)
    # <Response [200]> means it worked
    print(profiles_page)
    # try to print the profiles page and see if we successfully loged in
    # URL if correct: http://olympus.realpython.org/profiles
    # URL if WRONG: http://olympus.realpython.org/login
    print(profiles_page.url)

if __name__ == '__main__':
    # one_practice()
    # one_test()
    mech_soup()
sys.exit()