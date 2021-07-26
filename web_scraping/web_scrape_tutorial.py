# tutorial: https://realpython.com/python-web-scraping-practical-introduction/#scrape-and-parse-text-from-websites 

# import Python's standard library for working with URLs
from urllib.request import urlopen

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

