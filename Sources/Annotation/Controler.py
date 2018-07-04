import numpy as np
import cv2

_events = []
_frame = None

def event_shoot():
    cv2.setMouseCallback("image", shoot)
def event_free_kick():
    cv2.setMouseCallback("image", free_kick)
def event_penalty():
    cv2.setMouseCallback("image", penalty)
def event_nothing():
    cv2.setMouseCallback("image", nothing)

def nothing(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        global _events
        refPt = [(x - 80, y - 80)]
        refPt.append((x + 80, y + 80))
        _events.append({'name': "nothing", 'pos': refPt})

def penalty(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        global _events
        refPt = [(x - 400, y - 200)]
        refPt.append((x + 400, y + 200))
        cv2.rectangle(_frame['Image'], refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", _frame['Image'])
        _events.append({'name': "penalty", 'pos': refPt})

def free_kick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        global _events
        refPt = [(x - 150, y - 90)]
        refPt.append((x + 150, y + 90))
        _events.append({'name': "free_kick", 'pos': refPt})

def shoot(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        global _events
        refPt = [(x - 80, y - 80)]
        refPt.append((x + 80, y + 80))
        _events.append({'name': "shoot", 'pos': refPt})

class Controler:
    def __init__(self):
        self.events = []

    def get_event(self, frame):
        global _frame
        _frame = frame
        cv2.imshow('image', frame['Image'])
        goal = False
        keep = False
        nb = 1

        dic = {1048673: 10, 1048698: 24, 1048677: 100, 1048690: 250, 1114177: -10, 1114202: -24, 1114181: -100, 1114194: -250, 1113939: 1, 1113937: -1, 1113938: 3}
        dic_func = {102: event_free_kick, 115: event_shoot, 112: event_penalty, 119: event_nothing}
        #dic = {97: 10, 122: 24, 101: 100, 114: 250, 65601: -10, 65626: -24, 65605: -100, 65618: -250, 65363: 1, 65361: -1, 65362: 3}
        #dic_func = {102: event_free_kick, 115: event_shoot, 112: event_penalty, 119: event_nothing}
        while True:
            k = cv2.waitKey(33)
            # if k != -1:
            #     print(k)
            if k in dic:
                nb = dic[k]
                break
            elif k in dic_func:
                dic_func[k]()
            elif k == 1048679:#103: # Goal
                goal = True
                break
            elif k == 1048686:#110: # Nothing but keep
                keep = True
                break
            elif k == -1:
                continue
        self.events = _events
        return (nb, goal, keep)
