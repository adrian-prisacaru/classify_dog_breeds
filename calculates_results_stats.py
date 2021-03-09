#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create a function calculates_results_stats that calculates the
#          statistics of the results of the programrun using the classifier's model
#          architecture to classify the images. This function will use the
#          results in the results dictionary to calculate these statistics.
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best'
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the
#          how to calculate the counts and percentages for this function.
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics
#          (either a percentage or a count) where the key is the statistic's
#           name (starting with 'pct' for percentage or 'n' for count) and value
#          is the statistic's value.  This dictionary should contain the
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create
#       with this function
#
from functools import reduce


class Counter:
    def __init__(self, results_dic):
        """
        Count statistics for a results dictionary
        :param results_dic: results dictionary
        """
        self.results_dic = results_dic

    def count(self, condition):
        """
        Return the number of items that satisfy the provided condition
        :param condition: lambda (list: results_dic value) => bool
        :return: number of elements that satisfy the condition
        """
        return reduce(lambda acc, e: acc + 1 if condition(e) else acc, self.results_dic.values(), 0)


def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """
    # Replace None with the results_stats_dic dictionary that you created with
    # this function
    counter = Counter(results_dic)

    # Number of Images
    n_images = len(results_dic)

    # Number of Correct Dog matches
    n_correct_dogs = counter.count(lambda e: e[3] and e[4])

    # Number of Dog Images
    n_dogs_img = counter.count(lambda e: e[3])

    # Number of Correct Non-Dog matches
    n_correct_notdogs = counter.count(lambda e: not e[3] and not e[4])

    # Number of Not Dog Images
    n_notdogs_img = n_images - n_dogs_img

    # Number of Correct Breed matches
    n_correct_breed = counter.count(lambda e: e[2] and e[3])

    # Number of label matches
    n_matches = counter.count(lambda e: e[2])
    return {
        "n_images": n_images,
        "n_correct_dogs": n_correct_dogs,
        "n_dogs_img": n_dogs_img,
        "n_correct_notdogs": n_correct_notdogs,
        "n_notdogs_img": n_notdogs_img,
        "n_correct_breed": n_correct_breed,
        "n_matches": n_matches,

        # Percentage of correctly classified "dog" images
        "pct_correct_dogs": n_correct_dogs / n_dogs_img * 100,

        # Percentage of correctly classified "Non-dog" images
        "pct_correct_notdogs": n_correct_notdogs / n_notdogs_img * 100,

        # Percentage of correctly classified Dog Breed images
        "pct_correct_breed": n_correct_breed / n_dogs_img * 100,

        # Percentage of correctly Matched Images ( regardless if they are a dog)
        "pct_match": n_matches / n_images * 100
    }
