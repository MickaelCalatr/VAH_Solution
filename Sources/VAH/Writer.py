import threading
import os

from Sources.Common.folder import create

class Writer(object):
    singleton_lock = threading.Lock()
    singleton_instance = None
    video_list = {}
    path_to_save = "./Output/"
    path_tmp = path_to_save + "tmp/"
    filename = "video_list.txt"

    @classmethod
    def instance(cls):
        if not cls.singleton_instance:
            with cls.singleton_lock:
                if not cls.singleton_instance:
                    cls.singleton_instance = cls()
                    create(cls.path_tmp)
        return cls.singleton_instance

    def add_video(cls, start, end, thread_id):
        with cls.singleton_lock:
            times = str(start) + "-" + str(end)
            if thread_id not in cls.video_list:
                cls.video_list.update({thread_id: []})
            cls.video_list[thread_id].append(times)

    def create_final_video(cls, video_name, path):
        video_name = path + video_name
        os.system("ffmpeg -loglevel quiet -f concat -safe 0 -i " + cls.path_tmp + cls.filename + " -c copy " + cls.path_to_save + video_name)

    def save_video_file(cls):
        with cls.singleton_lock:
            cls.resize_videos()
            cls.extract_videos()
            times = cls.sort_videos()
            with open(cls.path_tmp + cls.filename, 'a') as out:
                for line in times:
                    out.write("file " + line + '.mp4\n')

    def extract_videos(cls):
        for key, values in cls.video_list.items():
            for times in values:
                video_name = times + ".mp4"
                (start, end) = times.split('-')
                end = str((int(end) - int(start)) / 25)
                start = str(int(start) / 25)
                cmd_line = "ffmpeg -loglevel quiet -r 25 -i " + key +" -ss " + start + " -c copy -t " + end + " " + cls.path_tmp + video_name
                os.system(cmd_line)

    def sort_videos(cls):
        times_list = []
        times_int = []
        for key, values in cls.video_list.items():
            times_list += values
        for times in times_list:
            start_time = int(times.split('-')[0])
            times_int.append(int(start_time))
        merged_videos = [x for _,x in sorted(zip(times_int, times_list))]
        return merged_videos


    def resize_videos(cls):
        for key, values in cls.video_list.items():
            if len(values) > 1:
                for i, times in enumerate(values):
                    if i < len(values) - 1:
                        current_start, current_end = cls.get_times(values, i)
                        next_start, next_end = cls.get_times(values, i + 1)
                        if next_start <= current_end or next_start - current_end < 200:
                            cls.video_list[key][i] = str(current_start) + "-" + str(next_end)
                            del cls.video_list[key][i + 1]

    def get_times(cls, arr, index):
        times_arr = arr[index].split('-')
        start = int(times_arr[0])
        end = int(times_arr[1])
        return start, end

    def close(cls):
        with cls.singleton_lock:
            delete(cls.path_to_save)
