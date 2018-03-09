import cv2

class Video:
    def __init__(self, name=None):
        super(Video, self).__init__()
        self.name = name
        self.video = None
        self.total_frames = 0
        self.frame = 0
        self.camera = None

    def load(self, name, camera):
        self.video = cv2.VideoCapture(name)
        self.camera = camera
        while not self.video.isOpened():
            print("Wait for the header...\nVideo name :", self.name)
            cv2.waitKey(1000)
            self.video = cv2.VideoCapture(name)
        self.frame = 0
        self.total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

    def set_position(self, nb):
        pos = self.frame - nb
        if pos < 0:
            pos = 0
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

    def get_frame(self, nb):
        if self.frame + nb >= self.total_frames:
            raise IndexError

        flag = False
        dic = {}
        while flag == False:
            self.video.set(cv2.CAP_PROP_POS_FRAMES, self.frame + nb - 1)
            flag, image = self.video.read()
            if not flag:
                print_points("Error during reading frame: " + str(self.frame))
                cv2.waitKey(1000)
            else:
                name = str(self.camera) + "." + str(self.frame)
                dic = {'Frame' : int(self.frame), 'Name' : name, 'Image': image}
                self.frame += nb
                break
        return dic
