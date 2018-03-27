import argparse

VERSION = "2.0.1"

class Config:
    def __init__(self):
        self.args = None

    def initialize(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--input", help = "Folder that contains videos.", required=True)
        ap.add_argument("-t", "--type", help = "Video type (1 = old video, 2 = news videos)", required=True, type=int)
        ap.add_argument("-c", "--camera", help = "Camera number", required=True, type=int)

        ap.add_argument("-o", "--output", help = "Folder that contains the images annotated.", default='./auto_output/')
        ap.add_argument("-s", "--step", help = "Step used to take block frame (step=2 : take one frame in two).", type=int, default=5)
        ap.add_argument("-l", "--label", help = "Label of th video (0 for not goal; 1 for goal).", type=int, default=0)
        ap.add_argument("-v", '--version', action='version', version='%(prog)s V' + str(VERSION))
        self.args = vars(ap.parse_args())
