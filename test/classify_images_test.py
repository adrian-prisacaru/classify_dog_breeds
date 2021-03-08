import os
import unittest
from classify_images import classify_images, compare_labels
from get_pet_labels import get_pet_labels

filename = 'Boston_terrier_02259.jpg'
images_dir = 'pet_images'


class ClassifyImagesTest(unittest.TestCase):
    def test_compare_labels(self):
        label = 'boston terrier'
        classifier_label = 'Boston bull, Boston terrier'
        self.assertEqual(compare_labels(label, classifier_label), 1)

    def test_classify_images(self):
        results_dic = get_pet_labels(images_dir)
        classify_images(images_dir, results_dic, 'vgg')
        self.assertEqual(results_dic[filename], ['boston terrier', 'Boston bull, Boston terrier', 1])
