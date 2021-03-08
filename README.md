## Udacity | Ai Programming with Python Nanodegree
### Project: Use a Pre-Trained Image Classifier to indetify dog breeds

Check pet images in a folder and determine which ones are dogs
and what breed using a pre-trained CNN model.

### Instalation

Python version: 3.6.13

Create a new environment with the required python version and run the
following command:

```shell
  pip install -r requirements.txt
```

### Run the program

```shell
  python check_images.py --dir pet_images --arch vgg --dogfile dognames.txt
```

### Run the tests

```shell
  pytest test
```
