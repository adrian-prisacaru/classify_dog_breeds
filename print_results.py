#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results
#          dictionary (results_dic).
#         This function inputs:
#            -The results dictionary as results_dic within print_results
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main.
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##

def any_misclassified_dogs(results_stats_dic):
    """
    Find if there are any misclassified dogs
    :param results_stats_dic: Results statistics dictionary
    :return: bool
    """
    return results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']


def any_misclassified_breeds(results_stats_dic):
    """
    Find if there are any misclassified breeds
    :param results_stats_dic: Results statistics dictionary
    :return: bool
    """
    return results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']


def misclassified_dogs(results_dic):
    """
    Find the misclassified dogs.
    Labels are misclassified as dogs when both labels aren't in agreement
    regarding whether or not an image is of a dog.
    :param results_dic: Results dictionary
    :return: dictionary of misclassified dogs [filename]: [label, classifier_label]
    """
    misclassified = {}
    for filename in results_dic:
        results = results_dic[filename]
        if sum(results[3:]) == 1:
            misclassified[filename] = [results[0], results[1]]
    return misclassified


def misclassified_breeds(results_dic):
    """
    Find the misclassified breeds.
    Labels have a misclassification of breeds of dog when both labels indicate that the image is a dog,
    but labels aren't in agreement regarding the dog's breed.
    :param results_dic: Results dictionary
    :return: dictionary of misclassified breeds [filename]: [label, classifoer_label]
    """
    misclassified = {}
    for filename in results_dic:
        results = results_dic[filename]
        if sum(results[3:]) == 2 and results[2] == 0:
            misclassified[filename] = [results[0], results[1]]
    return misclassified

# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function.
#       Notice that this function doesn't to return anything because it
#       prints a summary of the results using results_dic and results_stats_dic
#
def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if user indicates
    they want those printouts (use non-default values)
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
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value
      model - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and
                             False doesn't print anything(default) (bool)
      print_incorrect_breed - True prints incorrectly classified dog breeds and
                              False doesn't print anything(default) (bool)
    Returns:
           None - simply printing results.
    """
    print('\n\n---- Summary for CNN model', model, ' -----')
    print('Number of images:', results_stats_dic['n_images'])
    print('Number of dog images:', results_stats_dic['n_dogs_img'])
    print('Number of not dog images:', results_stats_dic['n_notdogs_img'])
    print('Percentage of correctly classified as dog:', results_stats_dic['pct_correct_dogs'])
    print('Percentage of correctly classified as not dog:', results_stats_dic['pct_correct_notdogs'])
    print('Percentage of correctly classified breeds:', results_stats_dic['pct_correct_breed'])
    print('Percentage of matching labels:', results_stats_dic['pct_match'])
    if print_incorrect_dogs:
        if any_misclassified_dogs(results_stats_dic):
            misclassified = misclassified_dogs(results_dic)
            print('\nMisclassified dogs:')
            for filename in misclassified:
                print("{}: '{}' misclassified as '{}'".format(filename, misclassified[filename][0], misclassified[filename][1]))
        else:
            print('\nNo misclassified dogs')
    if print_incorrect_breed:
        if any_misclassified_breeds(results_stats_dic):
            misclassified = misclassified_breeds(results_dic)
            print('\nMisclassified breeds:')
            for filename in misclassified:
                print("{}: '{}' misclassified as '{}'".format(filename, misclassified[filename][0], misclassified[filename][1]))
        else:
            print('\nNo misclassified breeds')

