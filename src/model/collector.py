from urllib.request import urlopen
from urllib.parse import quote

from bs4 import BeautifulSoup

acentos = 'àâáãéêíóõôú'


class Collector:
    def __init__(self, word: str):
        self.word = word
        base_url = 'https://www.separaremsilabas.com/index.php?lang=index.php&p='
        submit = '&button=Separa%C3%A7%C3%A3o+das+s%C3%ADlabas'
        self.word_url = word.replace('-', '')
        url = base_url + quote(self.word_url) + submit
        self.html = urlopen(url)

    @property
    def word_object(self):
        bs = BeautifulSoup(self.html, 'html.parser')
        string_req = str(bs.select('div font')[-1])
        filtred_string1 = self._filter_remove_tag_font(string_req)
        string_syllabale = self._indentify_syllabales(filtred_string1)
        return {
            self.word: string_syllabale,
        }

    def _filter_remove_tag_font(self, string_req: str):
        return string_req[string_req.find('>') + 1:string_req.find('</font')]

    def _indentify_syllabales(self, filtred_string1):
        return filtred_string1.replace('<strong>', '').replace('</strong>', '')

    def _acentuadas(self):
        cont = 0
        for letra in self.word:
            if letra in acentos:
                cont += 1
        return cont
