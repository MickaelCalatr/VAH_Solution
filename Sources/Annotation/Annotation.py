from Sources.Annotation.Configuration import Config
from Sources.Annotation.Detect import Detect
from Sources.Common.folder import create, delete
from Sources.Common.Video import Video
from Sources.Common.Json import Wrapper

class Annotation:
    def __init__(self):
        self.conf = Config()
        self.video = Video()
        self.detection = Detect(self.video)

    def run(self):
        try:
            self.initialize()
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


    def initialize(self):
        print("Initialize...")
        self.conf.initialize()
        name = self.conf.video_source.split("/")[-1]

        print("Loading data from :", name, "...")
        camera = name.split('.')[0]
        self.conf.camera = int(camera)
        self.conf.output_dir += camera + "/"
        create("." + self.conf.output_dir)
        self.video.load(self.conf.video_source, self.conf.camera)
        self.video.frame = self.conf.frame
        self.detection.initialize(self.conf)
        print("Loading data : Done!\n")

        print("Initialize : Done!\n")
