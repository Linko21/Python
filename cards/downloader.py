import json
import logging
import os
import time

import requests

log = logging.getLogger(__name__)


def download_data_from_url_to_file(url, target):
    if os.path.isfile(target):
        os.stat(target)
        log.info("file {} already exists, downloaded at {}, reusing this file".format(os.path.abspath(target), time.ctime(os.path.getmtime(target))))
        return target
    plain_data = download(url)
    json_object = json.loads(plain_data.text)
    json_formatted_str = json.dumps(json_object, indent=2)
    f = open(target, "w")
    f.writelines(json_formatted_str)
    f.close()
    log.info("downloaded {} to {}".format(url, os.path.abspath(target)))
    return target


def download(url: str):
    log.info("downloading " + url)
    resp = requests.get(url)
    log.info("downloaded " + url)
    return resp
