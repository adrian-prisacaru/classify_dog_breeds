import unittest
from calculates_results_stats import Counter, calculates_results_stats

results_dic = {
    'pet_1.jpg': ['dog_1', 'dog_1', 1, 1, 1],
    'pet_2.jpg': ['cat_1', 'cat_1', 1, 0, 0],
    'pet_3.jpg': ['dog_3', 'cat', 0, 1, 0],
    'pet_4.jpg': ['dog_4', 'dog_5', 0, 1, 1]
}


class CalculateResultsStatsTest(unittest.TestCase):
    def test_counter(self):
        counter = Counter(results_dic)
        self.assertEqual(counter.count(lambda e: e[0]), 4)
        self.assertEqual(counter.count(lambda e: e[2]), 2)

    def test_calculates_results_stats(self):
        results_stats = calculates_results_stats(results_dic)
        self.assertEqual(results_stats['n_images'], 4)
        self.assertEqual(results_stats['n_correct_dogs'], 2)
        self.assertEqual(results_stats['n_dogs_img'], 3)
        self.assertEqual(results_stats['n_correct_notdogs'], 1)
        self.assertEqual(results_stats['n_notdogs_img'], 1)
        self.assertEqual(results_stats['n_correct_breed'], 1)
        self.assertEqual(results_stats['n_matches'], 2)
        self.assertEqual(results_stats['pct_correct_dogs'], 2/3 * 100)
        self.assertEqual(results_stats['pct_correct_notdogs'], 1/1 * 100)
        self.assertEqual(results_stats['pct_correct_breed'], 1/3 * 100)
        self.assertEqual(results_stats['pct_match'], 2/4 * 100)
