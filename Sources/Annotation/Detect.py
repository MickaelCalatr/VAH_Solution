from Sources.Annotation.Time import Time
from Sources.Annotation.Controler import Controler
from Sources.Common.image import image_save
from Sources.Common.Json import Wrapper

import sys

class Detect:
    def __init__(self, video, output_dir="./"):
        self.output_dir = output_dir
        self.video = video
        self.controler = Controler()
        self.time = Time(self.video.total_frames)
        self.wrapper = None#Wrapper(self.video.get_frame(1)['Image'].shape, self.conf)


    def initialize(self, conf):
        self.time = Time(self.video.total_frames)
        self.wrapper = Wrapper(self.video.get_frame(1)['Image'].shape, conf)
        self.output_dir = conf.output_dir


    def run(self):
        next_frame = 1
        try:
            while True:
                frame = self.video.get_frame(next_frame)
                next_frame, goal, keep = self.controler.get_event(frame)
                if self.controler.events:
                    self.add_action(self.controler.events)
                    del self.controler.events[:]
                    keep = True
                if goal or keep:
                    self.wrapper.save_json(frame, goal)
                    image_save(self.output_dir, frame)
                self.print_states(frame)
        except IndexError:
            pass
        print()


    def add_action(self, events):
        for action in events:
            (xmin, ymin) = action['pos'][0]
            (xmax, ymax) = action['pos'][1]
            self.wrapper.add_box(xmin, ymin, xmax, ymax, action['name'])



    def print_states(self, frame):
        self.time.update()
        if self.time.need_to_print():
            sys.stdout.write("\033[F\033[J\033[F\033[J")
            print("Frame:\t\t", self.video.frame, "/", self.video.total_frames)
            print(self.time.timer(int(frame['Frame'])))
