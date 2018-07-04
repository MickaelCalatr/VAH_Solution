import time
import datetime

class Timer:
    def __init__(self):
        self.time_to_update = 5
        self.fps = 0
        self.old_frames = 0
        self.start = time.time()
        self.end = time.time()
        self.update_f = time.time()
        self.need_print = time.time()

    def need_to_print(self):
        update = self.end - self.need_print
        if update > self.time_to_update:
            self.need_print = self.end
            return True
        return False

    def update(self):
        self.end = time.time()

    def timer(self, frames):
        timer = int(self.end - self.start)
        update = self.end - self.update_f
        if update > 1:
            self.fps = int((frames - self.old_frames) / update)
            self.old_frames = frames
            self.update_f = self.end
        return str("Time:  " + time.strftime("%H:%M:%S", time.gmtime(timer)) + " \t Fps:  " + str(self.fps))

    def get_times(self):
        self.update()
        timer = int(self.end - self.start)
        return time.strftime("%H:%M:%S", time.gmtime(timer))
