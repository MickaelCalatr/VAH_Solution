import json
import cv2
from Sources.Common.position import get_position

class JsonBox:
    def __init__(self, action, x, y, w, z):
        self.xmin = x
        self.ymin = y
        self.xmax = w
        self.ymax = z
        self.action = action


class JsonCreator:
    def jdefault(o):
        return o.__dict__

    def __init__(self, boxes):
        self.boxes = boxes
        self.goal = None


    def save(self, frame, label, conf):
        name = str(frame['Name']) + ".json"
        (height, width, _) = frame['Image'].shape

        xmin, xmax, ymin, ymax = get_position(conf['type'], conf['camera'], width, height)
        # cv2.rectangle(frame['Image'], (xmin, ymin), (xmax, ymax), (255,0,0), 2)
        # cv2.imshow("lalala", frame['Image'])
        # cv2.waitKey(0)

        self.goal = JsonBox(label, xmin, ymin, xmax, ymax)
        with open(conf['output'] + name, 'w') as outfile:
            json.dump(self, outfile, default=lambda o: o.__dict__, indent=4)
            outfile.close


class Wrapper:
    def __init__(self, shape, conf):
        self.boxes = []
        (self.height, self.width, _) = shape
        self.conf = {'camera': conf.camera, 'type': conf.video_type, 'output': "." + conf.output_dir}

    def save_json(self, frame, keep):
        json = JsonCreator(self.boxes)
        if keep:
            goal = "goal_OK"
        else:
            goal = "goal_KO"
        json.save(frame, goal, self.conf)
        del self.boxes[:]

    def add_box(self, x, y, h, w, action):
        xmin = int((x * self.width) / 1280)
        ymin = int((y * self.height) / 720)
        xmax = int((h * self.height) / 720)
        ymax = int((w * self.width) / 1280)

        box = Box(action, xmin, ymin, xmax, ymax)
        self.boxes.append(box)
