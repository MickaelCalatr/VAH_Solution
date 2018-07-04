import logging
import urllib
import time
import sys


class Download:
    """docstring for Downloader."""
    def __init__(self, url, save_as):
        self.url = url
        self.save_as = save_as
        self.run = True

    def start(self):
        while self.run:
            try:
                urllib.urlretrieve(self.url, filename=save_as)
            except Exception:
                logging.warn("error downloading %s:" % (self.url))


class Downloader:
    """docstring for Downloader."""
    def __init__(self, time_to_wait=300, save_as='./Input/'):
        super(Downloader, self).__init__()
        self.time_to_wait = time_to_wait
        self.save_as = save_as
        self.threads = []


    def start(self, url, name):
        download = Download(url, self.save_as + name)
        self.threads.append(download)
        self.threads[-1].start()
        time.sleep(self.time_to_wait)

    # def stop(self):
    #
    # def finish(self):
