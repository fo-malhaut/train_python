import urllib.request
import sys
import os
import re
import numpy as np
import csv
from bs4 import BeautifulSoup

start = 2014
end = 2019

num = ""
num = sys.argv[1]
if len(num) != 4:
    print("argu is wrongs")
    sys.exit()

for year in range(start, end, 1):
    path = "/Users/s.watanabe/Desktop/develop app/predict_stock/data/%s" \
      % (num)
    if not os.path.isdir(path):
        os.mkdir(path)

    file = '%s/stock_%s_%s.csv' % (path, num, year)
    if os.path.isfile(file) and year != end-1:
        continue
    url = "https://kabuoji3.com/stock/%s/%s/" % (num, year)
    print(url)

    html = url.format(sys.argv[0])
    headers = {
      "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) \
      Gecko/20100101 Firefox/47.0"}
    request = urllib.request.Request(html, headers=headers)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response, "lxml")
    table = soup.find_all("td")
    box = []
    for ta in table:
        ta = str(ta)
        te = re.sub('</td>', '', ta)
        te = re.sub('<td>', '', te)
        box.append(te)
    box2 = np.reshape(box, (int(len(box)/7), 7))

#    if not os.path.exists(file):
    with open(file, "w") as f:
        # 改行コード（\n）を指定しておく
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(box2)
