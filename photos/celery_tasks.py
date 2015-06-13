#encoding:UTF-8
import urllib
from celery import task


@task
def download_file(url, name):
    urllib.urlretrieve(url, name)
    print "download!"