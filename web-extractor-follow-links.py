"""_summary_
This script first extracts the content from the homepage of the website and saves it as
"index.html" in the "example" directory. It then finds all the link tags on the homepage
"""

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Define the sample website URL
url = "http://localhost:3000/"

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
        css_response = requests.get(urljoin(url, css_url))
        css_file.write(css_response.text)
        css_file.close()

# Find all the image tags in the HTML and download their image files
image_tags = soup.find_all("img")
for tag in image_tags:
    image_url = tag.get("src")
    image_response = requests.get(urljoin(url, image_url))
    image_file = open("example/" + image_url.split("/")[-1], "wb")
    image_file.write(image_response.content)
    image_file.close()

# Find all the link tags in the HTML that point to first-level linked pages
page_links = []
link_tags = soup.find_all("a")
for tag in link_tags:
    link_url = tag.get("href")
    if link_url and link_url.startswith("/") and not link_url.startswith("//"):
        page_links.append(urljoin(url, link_url))

# Scrape the first-level linked pages
for page_url in page_links:
    # Send a GET request to the linked page URL and get the response
    response = requests.get(page_url)

    # Create a BeautifulSoup object from the linked page HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Save the linked page HTML file
    page_file = open("example/" + page_url.split("/")[-1], "w", encoding="utf-8")
    page_file.write(str(soup))
    page_file.close()

    # Find all the link tags in the linked page HTML and download their CSS files
    link_tags = soup.find_all("link")
    for tag in link_tags:
        if "stylesheet" in tag.get("rel", []):
            css_url = tag.get("href")
            css_file = open("example/" + css_url, "w", encoding="utf-8")
            css_response = requests.get(urljoin(page_url, css_url))
            css_file.write(css_response.text)
            css_file.close()

    # Find all the image tags in the linked page HTML and download their image files
    image_tags = soup.find_all("img")
    for tag in image_tags:
        image_url = tag.get("src")
        image_response = requests.get(urljoin(page_url, image_url))
        image_file = open("example/" + image_url.split("/")[-1], "wb")
        image_file.write(image_response.content)
        image_file.close()

print('Script is done Scrapping..!!!')