CONTENT:::
    1. About
    2. How to use
    3. TODO
    4. Anti-scrapping methods
    5. Disclaimer

1) ABOUT

This repo contains a number of scripts you can use to scrape and download websites for offline use. The scripts are in Python and use beautiful soup package for scrapping. Feel free to use and modify the scripts to suit your needs. 
The scripts perform the following actions:-
  1. Scrape and download the scrapped websites' css,javascript and images to your machine.
  2. Scrape a website that needs authentication.
  3. Scrape, translates to your desired language 
  4. Scrape to desired levels of links

2) HOW TO USE

Simple run the scripts in your terminal
 ```
  $ python web-scrapper-with-auth.py 

 ```

3) TODO

     1. Create a GUI tool for the scripts.
     2. Develop a web application for scrapping.
     3. Consolidate all the scripts into one file and use arguments parameters to
        to run the script

4) ANTI-SCRAPPING METHODS

There are several ways to prevent web scraping of a website, but none of them are foolproof. Here are some common techniques that can be used to reduce the likelihood of web scraping:

1. Use rate limiting: Limit the number of requests per unit of time from a single IP address. This     can be done using tools like django-ratelimit or django-brake.

2. Use CAPTCHA: Introduce a CAPTCHA system to verify that the user is a human and not a bot. This can be done using tools like Google reCAPTCHA.

3. Use user-agent verification: Check the User-Agent header of incoming requests to verify that they are legitimate. This can be done using tools like django-user-agents.

4. Use session-based authentication: Require users to log in to access content, and use session-based authentication to verify that they are authorized to access the content.

5. Use IP address blocking: Block IP addresses that are repeatedly making requests to your site or are otherwise suspicious.

6. Use obfuscation techniques: Make it harder for bots to parse your HTML by using techniques like minification, obfuscation, or dynamic content loading.

Keep in mind that these techniques may also make it more difficult for legitimate users to access your website, so you should use them judiciously and test their impact on the user experience.


5) DISCLAIMER

Web scraping is completely legal if you scrape data publicly available on the internet. But some kinds of data are protected by international regulations, so be careful scraping personal data, intellectual property, or confidential data.

Some organizations may not be happy with you scrapping data from their website so use this scripts responsibly or sort permission before running the scripts on someones website.