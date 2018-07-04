from PIL import Image

IMG = ".png"
def get_x_y(element):
    x = {'min': int(element['xmin']), 'max': int(element['xmax'])}
    y = {'min': int(element['ymin']), 'max': int(element['ymax'])}
    return x, y

def save_crop_image(src_image, dest_image_name, x, y):
    image = Image.open(src_image)
    croped_image = image.crop((x['min'], y['min'], x['max'], y['max']))
    croped_image.save(dest_image_name)
    croped_image.close()
    image.close()
    return dest_image_name

def save_full_image(src_image, dest_image_name):
    image = Image.open(src_image)
    image.save(dest_image_name)
    image.close()
    return dest_image_name

def add_crop_image(element, current_path, current_file, save_directory, saved_image):
    x, y = get_x_y(element)
    src_image_name = current_path + get_name(current_file)
    dest_image_name = str(saved_image) + IMG
    dest_image = save_directory + dest_image_name
    save_crop_image(src_image_name, dest_image, x, y)
    return dest_image_name

def add_full_image(current_path, current_file, save_directory, saved_image):
    src_image_name = current_path + get_name(current_file)
    dest_image_name = str(saved_image) + IMG
    dest_image = save_directory + dest_image_name
    save_full_image(src_image_name, dest_image)
    return dest_image_name

def save_images(full_image, crop_image, x, y):
    image = Image.open(full_image['src'])
    image.save(full_image['dest'])

    if crop_image != None:
        croped_image = image.crop((x['min'], y['min'], x['max'], y['max']))
        croped_image.save(crop_image['dest'])
        croped_image.close()
    image.close()


def add_images(element, path, current_file, save_directory, total_images):
    x, y = get_x_y(element)
    src_image = path + get_name(current_file)
    crop = None
    croped_image_name = ""
    add = 0

    if "Camera_3" not in path and "Camera_4" not in path:
        croped_image_name = str(total_images) + IMG
        dest_crop_image = save_directory + croped_image_name
        crop = {'src': src_image,'dest': dest_crop_image}
        add += 1

    full_image_name = str(total_images + add) + IMG
    dest_full_image = save_directory + full_image_name
    full = {'src': src_image, 'dest': dest_full_image}

    save_images(full, crop, x, y)
    return croped_image_name, full_image_name

def get_name(name):
    return name[:-5] + IMG
