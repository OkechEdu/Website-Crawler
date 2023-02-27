import requests
from bs4 import BeautifulSoup
from google.cloud import translate_v2 as translate

# Define the website URL to translate
url = "https://www.example.com"

# Define the target language
target_language = "hi"

# Set up the Google Cloud Translation API
translate_client = translate.Client()

# Get the website content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract the text content from the website
text = ""
for element in soup.find_all(text=True):
    text += f"{element} "

# Translate the text content to Hindi
result = translate_client.translate(text, target_language=target_language)

# Print the translated text
print(result["input"])
print(result["translatedText"])

