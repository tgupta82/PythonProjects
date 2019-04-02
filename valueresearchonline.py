import urllib3
import pandas as pd
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.valueresearchonline.com/funds/rankresult.asp?pg=ranking&cat=equityAll&exc=susp%2Cclose&returns=R3Month'
http = urllib3.PoolManager()

response = http.request('GET', url)
soup = BeautifulSoup(response, 'html.parser')
print(soup)
