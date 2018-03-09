import argparse

VERSION = "3.0.1"

class Config:
    def __init__(self):
        self.output_dir = "/output/" #TODO put name of the video_source
        self.video_source = []
        self.video_type = 1
        self.camera = 0

    def initialize(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--input", help = "Video", required=True, nargs='+')
        ap.add_argument("-t", "--type", help = "Video type (1 = old video, 2 = news videos)", required=True, type=int)
        ap.add_argument('--version', action='version', version='%(prog)s V' + str(VERSION))
        ap.add_argument("-n", "--nb", help = "Number of last files", type=int, default=0)

        args = vars(ap.parse_args())
        self.video_source = args["input"]
        self.frame = args["nb"]
        self.video_type = args['type']
