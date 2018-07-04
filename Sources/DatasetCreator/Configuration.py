import argparse

VERSION = "3.0.1"

class Config:
    def __init__(self):
        self.classes = {'shoot': 1, 'penalty': 2, 'nothing': 3, 'freekick': 4, 'goal_OK': 5}
        self.args = None

    def initialize(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--input", help = "Path to the files", required=True)
        ap.add_argument("-t", "--type", help = "Type of the dataset (angles of view)", nargs='+', default=None)
        ap.add_argument("-o", "--output_name", help = "Name of the JSON file output.", default="train.json")
        ap.add_argument('--version', action='version', version='%(prog)s V' + str(VERSION))
        self.args = vars(ap.parse_args())
