import os
import sys
import threading

from Sources.VAH.Time_calculator import Timer

class Printer(object):
    singleton_lock = threading.Lock()
    singleton_instance = None
    total_camera = 0
    timer = Timer()
    buffers = {}
    num_threads = len(buffers.items())

    @classmethod
    def instance(cls):
        if not cls.singleton_instance:
            with cls.singleton_lock:
                if not cls.singleton_instance:
                    cls.singleton_instance = cls()
        return cls.singleton_instance

    def initialize(cls, num_camera, cameras):
        with cls.singleton_lock:
            cls.total_camera = num_camera
            for x in cameras:
                cls.buffers.update({x: None})

    def add_to_print(cls, thread_id, frames):
        with cls.singleton_lock:
            if cls.timer.need_to_print():
                cls.buffers[thread_id] = frames
                for num_threads in range(len(cls.buffers.items())):
                    sys.stdout.write("\033[F\033[J")
                for thread, frames in cls.buffers.items():
                    msg = "Thread:  {0} \t  Frame: {1}"
                    print(msg.format(thread, frames))
            cls.timer.update()

    def del_thread(cls, thread_id):
        with cls.singleton_lock:
            if thread_id in cls.buffers:
                del cls.buffers[thread_id]
