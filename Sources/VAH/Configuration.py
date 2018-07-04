import configparser
import argparse

from Sources.Common.folder import check_path

VERSION = "2.0.1"

class Config:
    def __init__(self):
        self.args = None
        self.CNN = configparser.ConfigParser()
        self.CNN._interpolation = configparser.ExtendedInterpolation()
        self.tmp_directory = "./tmp/"
        self.config_file = "cnn.ini"
        self.initialize()

    def initialize(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--input", help = "Videos names.", required=True, nargs='+')
        ap.add_argument("-t", "--train_directory", help = "Directory containing the model.", default='./Model/')
        ap.add_argument("-o", "--output_directory", help = "Output directory.", default='./')
        ap.add_argument("-n", "--video_name", help = "Name of the final video.", type=str, default="result.mp4")
        ap.add_argument("-g", "--max_goals", help = "Maximum goals in one selected block to keep the section. (Have to be smaller than [block_frames])", type=int, default=25)
        ap.add_argument("-b", "--block_frames", help = "Block of frames selected for the CNN.", type=int, default=32)
        ap.add_argument("-s", "--step", help = "Step used to take block frame (step=2 : take one frame in two).", type=int, default=16)
        ap.add_argument("-ts", "--time_take", help = "Time keeps before and after the detected sequence (in seconds).", type=int, default=5)
        ap.add_argument("-v", '--version', action='version', version='%(prog)s V' + str(VERSION))
        self.args = vars(ap.parse_args())
        self.args['train_directory'] = check_path(self.args['train_directory'])
        self.CNN.read(self.args['train_directory'] + self.config_file)



    def get(self, section, key=None):
        result = {}
        options = self.CNN.options(section)
        for option in options:
            try:
                result[option] = self.smartcast(self.CNN.get(section, option))
                if result[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                result[option] = None
        if key == None:
            return result
        return result[key]


    def smartcast(self, value):
        tests = [int, float]
        for test in tests:
            try:
                return test(value)
            except ValueError:
                continue
        return value
