import os

def get_json_files(path):
    jsons = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)) and ".png" not in f:
            jsons.append(f)
    return jsons
