"""_summary_
This script sends a GET request to the sample website URL and extracts the HTML, CSS, and image
files from the response using the Beautiful Soup library. It then creates a directory called "example" 
and saves the website HTML file as "index.html" in that directory. It also finds all the link tags in 
the HTML that reference CSS files, downloads those CSS files, and saves them in the "example" directory.
Similarly, it finds all the image tags in the HTML, downloads those image files, and saves them in the 
"example" directory.

Note that this script only extracts the first-level content of the website and does not follow any
links to external pages. Additionally, the script may not work correctly for websites with complex 
layouts or dynamically generated content.
"""
import requests
from bs4 import BeautifulSoup
import os

# Define the sample website URL
url = "https://www.example.com"

# Send a GET request to the website URL and get the response
response = requests.get(url)

# Create a BeautifulSoup object from the website HTML
soup = BeautifulSoup(response.text, "html.parser")

# Create a directory to store the website files
if not os.path.exists("example"):
    os.mkdir("example")

# Save the website HTML file
html_file = open("example/index.html", "w", encoding="utf-8")
html_file.write(str(soup))
html_file.close()

# Find all the link tags in the HTML and download their CSS files
link_tags = soup.find_all("link")
for tag in link_tags:
    if "stylesheet" in tag.get("rel", []):
        css_url = tag.get("href")
        css_file = open("example/" + css_url, "w", encoding="utf-8")
        css_response = requests.get(css_url)
        css_file.write(css_response.text)
        css_file.close()

# Find all the image tags in the HTML and download their image files
image_tags = soup.find_all("img")
for tag in image_tags:
    image_url = tag.get("src")
    image_response = requests.get(image_url)
    image_file = open("example/" + image_url.split("/")[-1], "wb")
    image_file.write(image_response.content)
    image_file.close()
