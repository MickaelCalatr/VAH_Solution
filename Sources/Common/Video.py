import cv2
import time


class Video:
    def __init__(self, name=None, camera=0):
        super(Video, self).__init__()
        self.name = name
        self.video = None
        self.total_frames = 0
        self.frame = 0
        self.frame_pos = -1
        self.camera = camera

    def load(self, name, camera=0):
        self.video = cv2.VideoCapture(name)
        self.camera = camera
        self.name = name
        while not self.video.isOpened():
            print("Wait for the header...\nVideo name :", self.name)
            cv2.waitKey(1000)
            self.video = cv2.VideoCapture(name)
        self.frame = 0#158000
        self.frame_pos = -1
        self.video.set(cv2.CAP_PROP_POS_FRAMES, self.frame)
        self.total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

    def set_position(self, pos):
        # pos = self.frame - pos
        # if pos < 0:
        #     pos = 0
        self.frame = pos
        self.video.set(cv2.CAP_PROP_POS_FRAMES, pos)

    def take_point(self, index):
        if index < 0:
            index = 0
        self.frame = index
        return index

    def get_frames(self, block, step=1):
        frames = []
        flag = False
        for i in range(0, (block * step), step):
            self.video.set(cv2.CAP_PROP_POS_FRAMES, self.frame)
            flag, image = self.video.read()
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # cv2.imshow('image',image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            if not flag or self.frame_pos == self.video.get(cv2.CAP_PROP_POS_MSEC):
                raise IndexError
            else:
                frame = {'Index': self.frame, 'Image': image}
                frames.append(frame)
                self.frame += step
                self.frame_pos = self.video.get(cv2.CAP_PROP_POS_MSEC)
        return frames


    def get_frame(self, nb):
        flag = False
        dic = {}
        while flag == False:
            self.video.set(cv2.CAP_PROP_POS_FRAMES, self.frame + nb - 1)
            flag, image = self.video.read()
            if not flag:
                raise IndexError
            else:
                name = str(self.camera) + "." + str(self.frame)
                dic = {'Frame' : int(self.frame), 'Name' : name, 'Image': image}
                self.frame += nb
                break
        return dic


    def stop(self):
        self.video.release()
