def get_position(video_type, camera, width, height):
    if video_type == 1:
        return get_olds_positions(camera, width, height)
    elif video_type == 2:
        return get_news_positions(camera, width, height)
    return None

def get_news_positions(camera, width, height):
    if camera == 0:
        xmin = int((200 * width) / 1280)
        ymin = int((310 * height) / 720)
        xmax = int((750 * width) / 1280)
        ymax = int((600 * height) / 720)
    elif camera == 2:
        xmin = int((200 * width) / 1280)
        ymin = int((200 * height) / 720)
        xmax = int((600 * width) / 1280)
        ymax = int((400 * height) / 720)
    elif camera == 3 or camera == 4:
        xmin = 0
        ymin = 0
        xmax = width
        ymax = height
    elif camera == 1:
        xmin = int((700 * width) / 1280)
        ymin = int((200 * height) / 720)
        xmax = int((1100 * width) / 1280)
        ymax = int((400 * height) / 720)
    return (xmin, xmax, ymin, ymax)

def get_olds_positions(camera, width, height):
    if camera == 0:
        xmin = int((140 * width) / 1280)
        ymin = int((70 * height) / 720)
        xmax = int((490 * width) / 1280)
        ymax = int((300 * height) / 720)
    elif camera == 2:
        xmin = int((700 * width) / 1280)
        ymin = int((80 * height) / 720)
        xmax = int((1020 * width) / 1280)
        ymax = int((300 * height) / 720)
    elif camera == 3 or camera == 4:
        xmin = 0
        ymin = 0
        xmax = width
        ymax = height
    elif camera == 1:
        xmin = int((700 * width) / 1280)
        ymin = int((200 * height) / 720)
        xmax = int((1100 * width) / 1280)
        ymax = int((400 * height) / 720)
    return (xmin, xmax, ymin, ymax)
