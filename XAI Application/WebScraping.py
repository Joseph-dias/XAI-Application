import requests
from bs4 import BeautifulSoup

class WebsiteScraping:

    def __init__(self, url):
        self.url = url
        self.title = None
        self.body = None

    def getText(self):
        """
        Gets the raw text of the web page
        :return:
        """
        response = requests.get(self.url)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body("script", "style", "img", "input"):
            irrelevant.decompose()
        self.body = soup.body.get_text(separator='\n', strip=True)
        return self.title, self.body

