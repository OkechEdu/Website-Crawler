"""_summary_
In this modified script, we first create a session object using requests.Session().
We then send a POST request to authenticate using the provided username and password. 
The session cookie is automatically saved by the requests library.

Once authenticated, we send a GET request to the protected page using the session.get() method,
which includes the session cookie in the request. We then extract the content from the protected page
using the same method as before.

Note that the exact authentication process will depend on the website you're trying to scrape.
You may need to modify the authentication data or URL depending on the specifics of the site.
"""
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin


def download_css(css_url):
    try:
        r = requests.get(css_url)
        with open("example" + css_url, "w", encoding="utf-8") as css_file:
                css_file.write(r.text)
        # css_file = open("example/" + css_url, "w", encoding="utf-8")
        # css_file.write(r.text)
        # css_file.close()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading CSS: {e}")
        
        
def download_images(session, soup, url):
    # Create the images directory if it does not exist
    if not os.path.exists("example/images"):
        os.makedirs("example/images")

    # Find all img tags
    img_tags = soup.find_all("img")

    # Loop through each image tag and download the image
    for img in img_tags:
        img_url = img.get("src")
        if img_url.startswith("data:image"):
            continue
        image_response = session.get(urljoin(url, img_url))
        image_data = image_response.content

        # Save the image to the images directory
        with open(f"example/images/{os.path.basename(img_url)}", "wb") as f:
            f.write(image_data)



# Define the website URL and authentication credentials
url = "https://example.com"
username = "your-username"
password = "your-password"

# Create a session object and send a POST request to authenticate
session = requests.Session()
login_data = {
    "username": username,
    "password": password,
    "submit": "Login"
}
session.post(urljoin(url, "login"), data=login_data)

# Send a GET request to the protected page using the authenticated session
response = session.get(urljoin(url, "protected-page"))

# Create a BeautifulSoup object from the protected page HTML
soup = BeautifulSoup(response.text, "html.parser")

# Create a directory to store the website files
if not os.path.exists("example"):
    os.mkdir("example")

# Save the protected page HTML file
html_file = open("example/protected-page.html", "w", encoding="utf-8")
html_file.write(str(soup))
html_file.close()

# Find all the link tags in the HTML and download their CSS files
link_tags = soup.find_all("link")
for tag in link_tags:
    if "stylesheet" in tag.get("rel", []):
        css_link = soup.find("link", rel="stylesheet")
        if css_link is not None:
            css_url = urljoin(url, css_link['href'])
            download_css(css_url)
        else:
            pass
    pass
        # css_file = open("example/" + css_url, "w", encoding="utf-8")
        # css_response = session.get(urljoin(url, css_url))
        # css_file.write(css_response.text)
        # css_file.close()

download_images(session, soup, url)

# Find all the image tags in the HTML and download their image files
# image_tags = soup.find_all("img")
# for tag in image_tags:
#     image_url = tag.get("src")
#     image_response = session.get(urljoin(url, image_url))
#     image_file = open("example/" + image_url.split("/")[-1], "wb")
#     image_file.write(image_response.content)
#     image_file.close()
