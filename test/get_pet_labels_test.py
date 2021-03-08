import unittest
from get_pet_labels import label, get_pet_labels


class GetPetLabels(unittest.TestCase):
    def test_label(self):
        filename = 'Boston_terrier_02259.jpg'
        self.assertEqual(label(filename), 'boston terrier')
