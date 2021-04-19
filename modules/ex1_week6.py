from typing import Text
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from bf4 import BeautifulSoup;

class TextComparer:
    def __init__(self, url_list=[]):
        self.url_list = url_list


    def download(self, url, filename):
        try:
            r = requests.get(url)
            with open(filename, "a") as file:
                file.write(r.text)
        except:
            raise Exception("Given url not found")

    def multi_download(self):
        with ThreadPoolExecutor(max_workers=10) as ex:
            for url in self.url_list:
                ex.submit(self.download(url, url.split(".")[1]))

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.url_list) == 0:
            raise StopIteration
        return self.url_list.pop()

    def urllist_generator(self):
        while len(self.url_list) != 0:
            yield self.url_list.pop()

    def avg_vowels(self, text):
        all_vowels = "aeiouyæøå"
        vowels_count = 0
        all_words = text.split(" ")
        for word in all_words:
            for letter in word:
                if letter in all_vowels:
                    vowels_count += 1
        return vowels_count / len(all_words)

  

#tc = TextComparer(["https://www.facebook.com/", "https://www.google.com/"])

#print(tc.avg_vowels("hej med dig"))