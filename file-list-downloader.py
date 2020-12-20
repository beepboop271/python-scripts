# downloads files from a list of urls
# how you get the list of urls is up to you
import os
import time
import urllib

import requests


def download(url_list, save_dir, delay=0.1):
    if not os.path.isdir(save_dir):
        raise NotADirectoryError(f"not a directory: {save_dir}")
    for url in url_list:
        res = requests.get(url)
        print("got", url)

        # intended use case was downloading .pdf and .ppsx
        # files for a course, so i just took the real name of
        # the file in the url (the last part of the path), but
        # other use cases may prefer to just use
        # urllib.parse.unquote(url) or similar
        if "/" in url:
            real_name = urllib.parse.unquote(url.rsplit("/", 1)[1])
        else:
            real_name = url
        print("saving as", real_name)

        with open(os.path.join(save_dir, real_name), "wb") as f:
            print("wrote", f.write(res.content), "bytes")
        time.sleep(delay)
