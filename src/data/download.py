#!/usr/bin/env python3

# Downloads the sample datasets

import os
import shutil
import zipfile
import tempfile
import argparse
import requests

from src.paths import RAW_CORPUS

DATASET = 'https://bit.ly/2I93Z94'


def download(url=DATASET):
    _, path = tempfile.mkstemp(suffix="-"+url.split("/")[-1], prefix="download-")

    with open(path, 'wb') as fobj:
        req = requests.get(url, stream=True)
        for chunk in req.iter_content(chunk_size=4096):
            if chunk:
                fobj.write(chunk)

    return path


def unzip(path, target=RAW_CORPUS):
    if not os.path.exists(target):
        os.makedirs(target)

    try:
        zobj = zipfile.ZipFile(path, 'r')
        zobj.extractall(target)
        zobj.close()
    finally:
        os.remove(path)


def cleanup(target=RAW_CORPUS):
    # Move files from the sample directory to the corpus directory
    source = os.path.join(target, "sample")
    if os.path.exists(source):
        for name in os.listdir(source):
            src = os.path.join(source, name)
            dst = os.path.join(target, name)
            shutil.move(src, dst)

    # Remove extraneous directories
    for name in ("__MACOSX", "sample"):
        path = os.path.join(target, name)
        if os.path.exists(path):
            shutil.rmtree(path)


def main(args):
    """
    Downloads and extracts the sample corpus to disk.
    """
    if os.path.exists(RAW_CORPUS) and len(os.listdir(RAW_CORPUS)) > 1:
        print("corpus appears to already be downloaded")
        return

    unzip(download())
    cleanup()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="download sample datasets used in this tutorial",
        epilog="please report any issues on GitHub"
    )

    args = parser.parse_args()
    main(args)
