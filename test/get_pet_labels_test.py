import unittest
from get_pet_labels import label, get_pet_labels

filename = 'Boston_terrier_02259.jpg'
hidden_filename = '.test'
images_dir = 'pet_images'


class GetPetLabelsTest(unittest.TestCase):
    def test_label(self):
        self.assertEqual(label(filename), 'boston terrier')

    def test_get_pet_labels(self):
        results_dic = get_pet_labels(images_dir)
        self.assertEqual(results_dic[filename], [label(filename)])

    def test_ignore_hidden_files(self):
        results_dic = get_pet_labels(images_dir)
        self.assertNotIn(hidden_filename, results_dic.keys())
