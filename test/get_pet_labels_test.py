import unittest
from get_pet_labels import label, get_pet_labels

filename = 'Boston_terrier_02259.jpg'
images_dir = 'pet_images'


class GetPetLabelsTest(unittest.TestCase):
    def test_label(self):
        self.assertEqual(label(filename), 'boston terrier')

    def test_get_pet_labels(self):
        results_dic = get_pet_labels(images_dir)
        self.assertEqual(results_dic[filename], [label(filename)])
