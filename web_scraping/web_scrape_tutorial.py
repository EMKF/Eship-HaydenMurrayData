# tutorial: https://realpython.com/python-web-scraping-practical-introduction/#scrape-and-parse-text-from-websites

# import Python's standard library for working with URLs
from urllib.request import urlopen
import sys
import re

def aphrodite_web_scrape_tutorial1():
    # define the URL we want to access and open it
    url = "http://olympus.realpython.org/profiles/aphrodite"
    page = urlopen(url)
    # extract HTML from the webpage with .read() and then decode with .decode("utf-8")
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    # print the contents of the webpage
    print(html)
    # Method 1 for extracting text from HTML (NOTE: this gives us the index of the title tag, not the index of the title)
    title_index = html.find("<title>")
    print(title_index)
    # use this to get the index of the first letter in the title
    start_index = title_index + len("<title>")
    print(start_index)
    # use this to get the index of the closing </title> tag
    end_index = html.find("</title>")
    print(end_index)
    # FINALLY, extract the title by slicing the HTML string
    title = html[start_index:end_index]
    print(title)

def poseidon_web_scrape_tutorial2():
    url = 'http://olympus.realpython.org/profiles/poseidon'
    page = urlopen(url)
    html = page.read().decode("utf-8")
    start_index = html.find("<title>") + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    print(title)
    # the re library allows us to clean up some of the HTML (next function also does this, following tutorial)
    string = title
    string = re.sub("<.*>", "", string)
    print(string)

def dionysus_web_scrape_tutorial3():
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title)  # Remove HTML tags
    print(title)

def test1():
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html_text = page.read().decode("utf-8")
    print(html_text)
    for string in ["Name: ", "Favorite Color:"]:
        string_start_idx = html_text.find(string)
        text_start_idx = string_start_idx + len(string)

        next_html_tag_offset = html_text[text_start_idx:].find("<")
        text_end_idx = text_start_idx + next_html_tag_offset

        raw_text = html_text[text_start_idx: text_end_idx]
        clean_text = raw_text.strip(" \r\n\t")
        print(clean_text)


if __name__ == '__main__':
    # aphrodite_web_scrape_tutorial1()
    # poseidon_web_scrape_tutorial2()
    # dionysus_web_scrape_tutorial3()
    test1()