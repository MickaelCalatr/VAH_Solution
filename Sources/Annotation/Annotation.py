from Sources.Annotation.Configuration import Config
from Sources.Annotation.Detect import Detect
from Sources.Common.folder import create, delete
from Sources.Common.Video import Video
from Sources.Common.Json import Wrapper

class Annotation:
    def __init__(self):
        self.conf = Config()
        self.video = Video()
        self.detection = Detect(self.video, self.conf.output_dir)


    def initialize(self):
        print("Initialize...")
        self.conf.initialize()
        create("." + self.conf.output_dir)
        print("Initialize : Done!\n")


    def run(self):
        try:
            self.initialize()
            for video in self.conf.video_source:
                self.update(video)
                print("Processing...\n\n\n")
                self.detection.run()
                print("Processing : Done!\n")
            self.video.stop()
        except KeyboardInterrupt:
            print("\n\nEXIT: interrupt received, stoppin...")
        #except FileNotFoundError:
        #    print("ERROR: Video  [", conf.video_source,"]  doesn't exist.")


    def cleaning(self):
        print("Cleaning...")
        delete("tmp")
        print("Cleaning : Done!")
        print("Finish.")


    def update(self, video):
        name = video.split("/")[-1]
        print("Loading data from :", name, "...")
        self.conf.camera = int(name.split('.')[0])
        self.video.load(video, self.conf.camera)
        self.detection.update(self.conf)
        print("Loading data : Done!\n")
