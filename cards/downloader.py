import json
import os
import time

import requests


def download_data_from_url_to_file(url, target):
    if os.path.isfile(target):
        os.stat(target)
        print("{} already exists, downloaded at {}, use this file".format(os.path.abspath(target), time.ctime(os.path.getmtime(target))))
        return
    plain_data = download(url)
    json_object = json.loads(plain_data.text)
    json_formatted_str = json.dumps(json_object, indent=2)
    f = open(target, "w")
    f.writelines(json_formatted_str)
    f.close()
    print("downloaded {} to {}".format(url, os.path.abspath(target)))


def download(url: str):
    print("downloading " + url)
    resp = requests.get(url)
    print("downloaded " + url)
    return resp
