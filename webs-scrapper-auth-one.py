"""_summary_
This code uses a try-except block to catch any exceptions that might be raised when trying to download
the CSS file. If an exception is raised, it prints an error message to the console. 
You could modify this behavior to suit your needs, such as writing the error message to a log file or 
displaying a message to the user.
"""
import requests

def download_css(css_url):
    try:
        r = requests.get(css_url)
        css_file = open("example/" + css_url, "w", encoding="utf-8")
        css_file.write(r.text)
        css_file.close()
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

