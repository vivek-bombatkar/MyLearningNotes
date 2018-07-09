# TensorFlow<sup>TM</sup> notMNIST predict (recognise handwriting)


## Installation & Setup

### Overview
This project uses the notMNIST tutorial from the TensorFlow website. The tutorial uses a deep learning model.

This projects consists of two scripts: 

1. _createModel.py_ – creates a model model.ckpt file based on the  tutorial.
3. *predict.py* – uses the model.ckpt (beginners tutorial) file to predict the correct integer form a handwritten letter in a .png file.

### Dependencies
The following Python libraries are required.

- tensorflow - [TensorFlow](https://www.tensorflow.org/)

### Installing TensorFlow
Of course TensorFlow needs to be installed. The [TensorFlow website](https://www.tensorflow.org/versions/master/get_started/index.html) has a good manual .


### The python scripts
The easiest way the use the scripts is to put all four scripts in the same folder. If TensorFlow is installed correctly and the images to train the model are present in that folder with the name notMNIST_large, you are good to go.

## Running
Running is based on the steps:

1. create the model file
2. create an image file containing a handwritten letter
3. predict the character 

### 1. create the model file
The easiest way is to cd to the directory where the python files are located. Then run:

```python createModel.py```


to create the model based on the notMNIST beginners tutorial.

### 2. create an image file
You have to create a PNG file that contains a handwritten character. The background has to be white and the letter has to be black. Any paint program should be able to do this. Also the image has to be auto cropped so that there is no border around the letter.

### 3. predict the character
The easiest way again is to put the image file from the previous step (step 2) in the same directory as the python scripts and cd to the directory where the python files are located. 

The predict scripts require one argument: the file location of the image file containing the handwritten letter. For example when the image file is letter.png’ and is in the same location as the script, run:

```python predict.py letter.png’```

The script, predict.py, uses the model.ckpt file created by the createModel.py script.


