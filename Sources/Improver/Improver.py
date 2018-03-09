from Sources.Improver.Configuration import Config
from Sources.Common.Video import Video
from Sources.Common.position import get_position
from Sources.Common.Json import JsonCreator
from Sources.Common.image import image_save
from Sources.Common.folder import create

import sys

class Improver(object):
    """docstring for Improver."""
    def __init__(self):
        super(Improver, self).__init__()
        self.video = Video()
        self.json = JsonCreator([])
        self.conf = Config()

    def run(self):
        self.conf.initialize()
        create(self.conf.args['output'])
        total_frames = 0
        frames_done = 0
        try:
            print("Starting, video :", self.conf.args['input'], '\n')
            self.video.load(self.conf.args['input'], self.conf.args['camera'])
            total_frames += self.video.total_frames
            while True:
                self.print_state(frames_done, total_frames)
                frame = self.video.get_frame(self.conf.args['step'])
                (height, width, _) = frame['Image'].shape
                xmin, xmax, ymin, ymax = get_position(self.conf.args['type'], self.conf.args['camera'], width, height)
                x = {'min': xmin, 'max': xmax}
                y = {'min': ymin, 'max': ymax}
                self.json.save(frame, "goal_KO", self.conf.args)
                image_save(self.conf.args['output'][1:], frame)
                frames_done += self.conf.args['step']
        except IndexError:
            pass

    def print_state(self, frame, total):
        sys.stdout.write("\033[F\033[J")
        print("Frame:\t\t", frame, "/", total)
