import requests
from bs4 import BeautifulSoup


class GetData():
    def __init__(self, urltoscrap,urlparameter):
        self.urltoscrap = urltoscrap
        self.urlparameter = urlparameter

    def doc_req(self):
        return requests.get(self.urltoscrap,params=self.urlparameter)

    def html_parser(self):
        return BeautifulSoup(self.doc_req().text,'html.parser')
