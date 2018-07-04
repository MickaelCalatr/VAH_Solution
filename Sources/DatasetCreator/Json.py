import json

class Elem:
    def __init__(self, name, label_text, label_id):
        self.filename = name
        self.label = {'text': label_text, 'id': label_id}

class Json:
    def jdefault(o):
        return o.__dict__

    def add_elem(self, name, label_text, label_id):
        elem = Elem(name, label_text, label_id)
        self.elements.append(elem)

    def save_json(self, directory, total_images):
        self.total_images = total_images
        with open(directory, 'w') as outfile:
            json.dump(self, outfile, default=lambda o: o.__dict__, indent=4)

    def __init__(self):
        self.elements = []
        self.total_images = 0
