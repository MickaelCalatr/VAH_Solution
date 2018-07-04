import os
import io
import sys
import json

from Sources.DatasetCreator.Json import *
from Sources.DatasetCreator.Configuration import Config
from Sources.DatasetCreator.image import add_images
from Sources.DatasetCreator.ressources import *
from Sources.Common.folder import check_path, create

#IMAGES_DIRECTORY = FLAGS['output_directory'] + "Images/"

class Creator:
    def __init__(self):
        self.config = Config()
        self.json = Json()
        self.save_directory = "./Dataset/Images/"
        self.train_directory = "./Dataset/"
        self.directories = []

    def initialize(self):
        print("Initialisation: ...")
        create(self.save_directory)
        self.config.initialize()
        self.init_path(self.config.args['input'])
        sys.stdout.write("\033[F\033[J")
        print("Initialisation: Done !")

    def init_path(self, path):
        for x in os.listdir(path):
            next_path = path + "/" + x
            if os.path.isdir(next_path):
                self.init_path(next_path)
            else:
                add = True
                path = "/".join(next_path.split('/')[:-1]) + "/"
                if self.config.args['type'] != None:
                    for camera in self.config.args['type']:
                        if camera in path:
                            add = True
                        else:
                            add = False
                        if add:
                            self.directories.append(path)
                else:
                    self.directories.append(path)
                break;

    def run(self):
        self.initialize()
        total_images = 0
        for path in self.directories:
            path = check_path(path)
            print("Start in:", path, '\n')

            json_files = get_json_files(path)
            current_directory = path.split("/")[-3] + "/"
            save_directory = self.save_directory + current_directory
            create(save_directory)

            for f in json_files:
                print_state(f, total_images)

                with open(os.path.join(path, '{}'.format(f))) as jsonFile:
                    data = json.load(jsonFile)

                    for element in data['boxes']:
                        dest_image = add_crop_image(element, path, f, save_directory, total_images)
                        creator.add_elem(dest_image, element['action'], self.class_text_to_int(element['action']))
                        saved_image += 1

                    crop_image, full_image = add_images(data['goal'], path, f, save_directory, total_images)
                    if "Camera_3" not in path and "Camera_4" not in path:
                        crop_image = "Images/" + current_directory + crop_image
                        self.json.add_elem(crop_image, data['goal']['action'], self.class_text_to_int(data['goal']['action']))
                        total_images += 1
                    full_image = "Images/" + current_directory + full_image
                    self.json.add_elem(full_image, data['goal']['action'], self.class_text_to_int(data['goal']['action']))
                    total_images += 1
            self.json.save_json(self.train_directory + self.config.args['output_name'], total_images)
            print()
        output_path = os.path.join(os.getcwd(), (self.train_directory[1:] + self.config.args["output_name"]))
        print('Successfully created the JSON : {}'.format(output_path))
        print('Total Images : {}', total_images)

    def class_text_to_int(self, row_label):
        if row_label in self.config.classes:
            return self.config.classes[row_label]
        return 0


def print_state(frame, total):
    sys.stdout.write("\033[F\033[J")
    print("File: \t", frame, "/", total)
