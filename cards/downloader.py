import json
import logging
import os
import time

import requests

log = logging.getLogger(__name__)


def download_data_from_url_to_file(url, target):
    parent_dir = os.path.dirname(target)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    if os.path.isfile(target):
        log.info("file {} already exists, downloaded at {}, reusing this file".format(os.path.abspath(target), time.ctime(os.path.getmtime(target))))
        return target
    log.info("downloading " + url + " to " + os.path.abspath(target))
    plain_data = requests.get(url)
    json_object = json.loads(plain_data.text)
    json_formatted_str = json.dumps(json_object, indent=2)
    f = open(target, "w")
    f.writelines(json_formatted_str)
    f.close()
    log.info("downloaded {} to {}".format(url, os.path.abspath(target)))
    return target
