from Sources.VAH.CNN import CNN
from Sources.VAH.Interpreter import Interpreter
from Sources.VAH.Time_calculator import Timer
from Sources.Common.Video import Video

import threading


class Detection(threading.Thread):
    def __init__(self, writer, printer, config, video_name):
        threading.Thread.__init__(self)#super(Detection, self).__init__()
        self.num_frames = config.args['block_frames']
        self.step = config.args['step']
        self.time_on_side = config.args['time_take'] * 25

        self.CNN = CNN(config.get('Image'),
                       config.get('CNN', 'model'),
                       config.args['directory'])
        self.video = Video()
        self.video.load(video_name)
        self.id = video_name
        #self.camera = camera
        self.printer = printer
        self.saver = writer
        self.interpreter = Interpreter(config.args['max_goals'])
        self.timer = Timer()


    def analyse(self, num_frames, step):
        frames = self.video.get_frames(num_frames, step)
        results = self.detection(frames)
        return self.interpreter.analyse(results)

    def run(self):
        try:
            while True:
                frames = self.video.get_frames(self.num_frames, self.step)
                results = self.detection(frames)
                goal = self.interpreter.are_goals(results)
                if goal:
                    save_frame = self.video.frame
                    position = self.interpreter.first_goal(results)
                    self.video.set_position(frames[position]['Index'])
                    if self.analyse(self.num_frames, 3):
                        self.video.set_position(frames[position]['Index'])
                        self.save_sequence(frames[position])
                    if save_frame > self.video.frame:
                        self.video.set_position(save_frame)
                self.printer.add_to_print(self.id, self.video.frame)
        except IndexError:
            self.printer.del_thread(self.id)
        finally:
            print("Video : ", self.id, " ----> Finished in :", self.timer.get_times(), "\n\n")


    def save_sequence(self, frame):
        results = []
        print("saved")
        start_point = self.video.take_point(frame['Index'] - self.time_on_side)
        while True:
            frames = self.video.get_frames(self.num_frames, 5)
            results = self.detection(frames)
            if self.interpreter.analyse(results) == False:
                break
            self.printer.add_to_print(self.id, self.video.frame)
        last_goal = self.interpreter.last_goal(results)
        end_point = self.video.take_point(frames[last_goal]['Index'] + self.time_on_side)
        self.video.set_position(end_point)
        self.saver.add_video(start_point, end_point, self.id)

    def detection(self, frames):
        results = self.CNN.run(frames)
        results = list(results)
        return results


#
# class Detection(object):
#     def __init__(self, saver, config, video_name, camera):
#         super(Detect, self).__init__()
#         self.num_frames = config.args['block_frames']
#         self.step = config.args['step']
#         self.time_on_side = self.config.args['time_take'] * 25
#
#         self.CNN = CNN(config.get('Image'),
#                        config.get('CNN', 'model'),
#                        config.args['directory'])
#         self.video = Video()
#         self.video.load(video_name)
#         self.camera = camera
#         self.saver = saver#Saver(config.args['max_threads'], config.args['video_name'])
#         self.interpreter = Interpreter(config.args['max_goals'])
#
#
#     def analyse(self, num_frames, step):
#         frames = self.video.get_frames(num_frames, step)
#         results = self.detection(frames)
#         return self.interpreter.analyse(results)
#
#     def run(self):
#         self.saver.update_file(self.video.name) #TODO rewrite saver class
#         try:
#             while True:
#                 if self.analyse(self.num_frames, self.step):
#                     save_frame = self.video.frame
#                     position = self.interpreter.first_goal(results)
#                     self.video.set_position(frames[position]['index'])
#                     if self.analyse(self.num_frames, 3):
#                         self.video.set_position(frames[position]['index'])
#                         self.save_sequence(frames[position])
#                     if save_frame > self.video.frame:
#                         self.video.set_position(save_frame)
#         except IndexError:
#             pass
#         self.saver.save_final_video()
#         print("Finished !")
#
#     def save_sequence(self, frame):
#         results = []
#         start_point = self.video.take_point(frame['index'] - self.time_on_side)
#         while True:
#             frames = self.video.get_frames(self.num_frames, 5)
#             results = self.detection(frames)
#             if self.interpreter.analyse(results) == False:
#                 break
#         last_goal = self.interpreter.last_goal(results)
#         end_point = self.video.take_point(frames[last_goal]['index'] + self.time_on_side)
#         self.video.set_position(end_point)
#         self.saver.save(start_point, end_point)
#
#     def detection(self, frames):
#         results = self.CNN.run(frames)
#         results = list(results)
#         return results
