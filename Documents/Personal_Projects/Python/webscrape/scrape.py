#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'
}

LoginData = {
    'ctl00$cpBody$UserLoginUc$Login1$UserName': 'stevenmcgown1@gmail.com',
    'ctl00$cpBody$UserLoginUc$Login1$Password': '\y;v2z!Su`<^*r84',
    'ctl00$cpBody$UserLoginUc$Login1$LoginButton': 'Login'
}
file = open("test.html", "a")
for i in range(2, 66):
  with requests.Session() as s:

      url = "https://free-braindumps.com/login.html?ReturnURL=/amazon/free-saa-c02-braindumps.html?p=" + \
          str(i)
      r = s.get(url, headers=headers)
      soup = BeautifulSoup(r.content, 'html.parser')

      LoginData['__VIEWSTATE'] = soup.find(
          'input', attrs={'id': '__VIEWSTATE'})['value']
      LoginData['__VIEWSTATEGENERATOR'] = soup.find(
          'input', attrs={'id': '__VIEWSTATEGENERATOR'})['value']
      LoginData['__EVENTVALIDATION'] = soup.find(
          'input', attrs={'id': '__EVENTVALIDATION'})['value']

      r = s.post(url, data=LoginData, headers=headers)

      soup = BeautifulSoup(r.content, 'html.parser')
      PageQuestions = soup.findAll(
          "div", attrs={"class": "product-info-box questions"})
      file.write(str(PageQuestions))
