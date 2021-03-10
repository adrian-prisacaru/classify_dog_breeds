import unittest

from calculates_results_stats import calculates_results_stats
from print_results import any_misclassified_dogs, any_misclassified_breeds, misclassified_dogs, misclassified_breeds

filename = 'Boston_terrier_02259.jpg'
images_dir = 'pet_images'

results_dic = {
    'pet_1.jpg': ['dog_1', 'dog_1', 1, 1, 1],
    'pet_2.jpg': ['cat_1', 'cat_1', 1, 0, 0],
    'pet_3.jpg': ['dog_3', 'cat', 0, 1, 0],
    'pet_4.jpg': ['dog_4', 'dog_5', 0, 1, 1]
}
results_stats_dic = calculates_results_stats(results_dic)

# no misclassifications
results_dic_2 = {
    'pet_5.jpg': ['dog_5', 'dog_5', 1, 1, 1]
}
results_stats_dic_2 = calculates_results_stats(results_dic_2)


class PrintResultsTest(unittest.TestCase):
    def test_any_misclassified_dogs(self):
        self.assertTrue(any_misclassified_dogs(results_stats_dic))
        self.assertFalse(any_misclassified_dogs(results_stats_dic_2))

    def test_any_misclassified_breeds(self):
        self.assertTrue(any_misclassified_breeds(results_stats_dic))
        self.assertFalse(any_misclassified_breeds(results_stats_dic_2))

    def test_misclassified_dogs(self):
        self.assertEqual(misclassified_dogs(results_dic), {'pet_3.jpg': ['dog_3', 'cat']})

    def test_misclassified_breeds(self):
        self.assertEqual(misclassified_breeds(results_dic), {'pet_4.jpg': ['dog_4', 'dog_5']})
