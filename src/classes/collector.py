from urllib.request import urlopen
from bs4 import BeautifulSoup


class Collector:
    def __init__(self, word: str):
        base_url = 'https://www.separaremsilabas.com/index.php?lang=index.php&p='
        submit = '&button=Separa%C3%A7%C3%A3o+das+s%C3%ADlabas'
        self.url = base_url + word + submit
        self.html = urlopen(self.url)

    @property
    def word_object(self):
        bs = BeautifulSoup(self.html, 'html.parser')
        string_req = bs.select('div font')[-1]
        print(string_req)
        # separated_sylabale = string_req[string_req]
        return None