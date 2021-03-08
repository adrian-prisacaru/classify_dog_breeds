import unittest

from adjust_results4_isadog import adjust_results4_isadog, generate_dog_names, is_dog
from classify_images import classify_images
from get_pet_labels import get_pet_labels

filename = 'Boston_terrier_02259.jpg'
cat_filename = 'cat_01.jpg'
images_dir = 'pet_images'
dogfile = 'dognames.txt'


class AdjustResults4IsADogTest(unittest.TestCase):
    def test_generate_dog_names(self):
        dog_names = generate_dog_names(dogfile)
        self.assertIn('chihuahua', dog_names)
        self.assertIn('maltese dog', dog_names)
        self.assertIn('maltese terrier', dog_names)

    def test_is_dog(self):
        dog_names = generate_dog_names(dogfile)
        self.assertTrue(is_dog('maltese terrier', dog_names))
        self.assertTrue(is_dog('Boston bull, Boston terrier', dog_names))

    def test_adjust_results4_isadog(self):
        results_dic = get_pet_labels(images_dir)
        classify_images(images_dir, results_dic, 'vgg')
        adjust_results4_isadog(results_dic, dogfile)
        self.assertEqual(results_dic[filename], ['boston terrier', 'Boston bull, Boston terrier', 1, 1, 1])
        self.assertEqual(results_dic[cat_filename], ['cat', 'lynx', 0, 0, 0])

