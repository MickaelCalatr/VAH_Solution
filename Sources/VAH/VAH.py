import os

from Sources.VAH.Configuration import Config
from Sources.VAH.Detection import Detection
from Sources.VAH.Downloader import Downloader
from Sources.VAH.Writer import Writer
from Sources.VAH.Printer import Printer

class VideoHighlight:
    """docstring for VideoHighlight."""
    def __init__(self):
        super(VideoHighlight, self).__init__()
        self.conf = Config()
        self.cameras = []
        self.downloader = Downloader(save_as='./')
        self.workers = []

    def download(self):
        video = 0
        for camera in self.conf.args['input']:
            if os.path.exists(camera):
                self.cameras.append(camera)
            else:
                video_name = video_name
                self.downloader.start(camera, video_name)
                self.cameras.append(video_name)
                video += 2


    def run(self):
        class Saver(Writer):
            pass
        class Print(Printer):
            pass
        writer = Saver.instance()
        printer = Print.instance()
        printer.initialize(len(self.conf.args['input']), self.conf.args['input'])
        self.download()
        for video_name in self.cameras:
            detection = Detection(writer, printer, self.conf, video_name)
            self.workers.append(detection)
        for thread in self.workers:
            thread.start()
        for thread in self.workers:
            thread.join()
        writer.save_video_file()
        writer.create_final_video(self.conf.args['video_name'], './')
