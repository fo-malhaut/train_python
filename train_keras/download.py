from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os
import time
import sys

# APIキーの情報
key = "120867a099a58161cbdd129b8ce5214c"
sercret = "cb199c65ea103f48"
wait_time = 1

# 保存フォルダ
towername = sys.argv[1]
savedir = "./" + towername

flickr = FlickrAPI(key, sercret, format='parsed-json')
result = flickr.photos.search(
    text=towername,
    per_page=600,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q, licence'
)

photos = result['photos']
# 返り値を取得する
# pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    print("Download pict:" + str(i))
    if os.path.exists(filepath):
        continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
