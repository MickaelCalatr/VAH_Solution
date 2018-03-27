import numpy as np
import tensorflow as tf
from scipy import misc

class CNN(object):
    def __init__(self, image_config, model_name, train_directory):
        super(CNN, self).__init__()
        self.model = model_name
        self.train_directory = train_directory + "train/"
        self.image_size = image_config['size']
        self.image_channels = image_config['channels']
        self.sess = tf.Session()
        self.softmax = None
        self.x = None
        self.y = None
        self.initialize()

    def initialize(self):
        saver = tf.train.import_meta_graph(self.train_directory + self.model)
        saver.restore(self.sess, tf.train.latest_checkpoint(self.train_directory))
        graph = tf.get_default_graph()

        self.softmax = graph.get_tensor_by_name("softmax/softmax:0")
        self.x = graph.get_tensor_by_name("input/x:0")
        self.y = graph.get_tensor_by_name("input/y:0")


    def preprocessing_image(self, frames):
        images = []
        for frame in frames:
            image = misc.imresize(frame['Image'], (self.image_size, self.image_size, self.image_channels))
            image = image.astype(np.float32)
            image = np.multiply(image, 1.0/255.0)
            images.append(image)
        images = np.array(images)
        return images

    def run(self,frames):
        images = self.preprocessing_image(frames)
        batch_size = len(images)

        x_batch = images.reshape(batch_size, self.image_size, self.image_size, self.image_channels)
        y_batch = np.zeros((batch_size, 2))

        feed_dict_testing = {self.x: x_batch, self.y: y_batch}
        results = self.sess.run(self.softmax, feed_dict=feed_dict_testing)
        return results
