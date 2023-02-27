from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from google.cloud import translate_v2 as translate
from io import BytesIO
from PIL import Image

# Define the website URL to translate
url = "https://www.example.com"

# Define the target language
target_language = "hi"

# Set up the Google Cloud Translation API
translate_client = translate.Client()

# Set up the Chrome driver options
options = Options()
options.add_argument("--headless")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

# Navigate to the website URL
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

# Extract the text content from the website
text = driver.find_element_by_tag_name("body").text

# Extract the image content from the website
images = driver.find_elements_by_tag_name("img")
image_text = ""
for image in images:
    image_url = image.get_attribute("src")
    image_data = requests.get(image_url).content
    image_file = BytesIO(image_data)
    image_object = Image.open(image_file)
    image_text += pytesseract.image_to_string(image_object)

# Translate the text content to Hindi
result = translate_client.translate(text, target_language=target_language)

# Translate the image content to Hindi
image_result = translate_client.translate(image_text, target_language=target_language)

# Print the translated text
print(result["input"])
print(result["translatedText"])

# Print the translated image text
print(image_result["input"])
print(image_result["translatedText"])

# Quit the Chrome driver
driver.quit()

##has to be refatored