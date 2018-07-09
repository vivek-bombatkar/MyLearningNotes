import tensorflow as tf
import os
from random import randint
import numpy as np

folders = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
root = "."
datasetFolder = "/notMNIST_small"

def getNumber(alphabet):
    if(alphabet == "A"):
        return np.eye(10, dtype=np.float32)[0]
    if(alphabet == "B"):
        return np.eye(10, dtype=np.float32)[1]
    if(alphabet == "C"):
        return np.eye(10, dtype=np.float32)[2]
    if(alphabet == "D"):
        return np.eye(10, dtype=np.float32)[3]    
    if(alphabet == "E"):
        return np.eye(10, dtype=np.float32)[4]
    if(alphabet == "F"):
        return np.eye(10, dtype=np.float32)[5]
    if(alphabet == "G"):
        return np.eye(10, dtype=np.float32)[6]
    if(alphabet == "H"):
        return np.eye(10, dtype=np.float32)[7]
    if(alphabet == "I"):
        return np.eye(10, dtype=np.float32)[8]
    if(alphabet == "J"):
        return np.eye(10, dtype=np.float32)[9]

    
def getListOfImages():
    global folders
    global root
    global datasetFolder
    allImagesArray = np.array([], dtype=np.str)
    allImagesLabelsArray = np.array([], dtype=np.str)
    for folder in folders:
        print("Loading Image Name of ", folder)
        currentAlphabetFolder = root+datasetFolder+"/"+folder+"/"
        imagesName = os.listdir(currentAlphabetFolder)
        allImagesArray = np.append(allImagesArray, imagesName)
        for i in range(0, len(imagesName)):
            if(i % 500 == 0):
                print("progress -> ", i)
            allImagesLabelsArray = np.append(allImagesLabelsArray, currentAlphabetFolder)
    return allImagesArray, allImagesLabelsArray

def shuffleImagesPath(imagesPathArray, imagesLabelsArray):
    print("Size of imagesPathArray is: ", len(imagesPathArray))
    for i in range(0, 100000):
        if(i % 1000 == 0):
            print("Shuflling in Progress -> ", i)
        randomIndex1 = randint(0, len(imagesPathArray)-1)
        randomIndex2 = randint(0, len(imagesPathArray)-1)
        imagesPathArray[randomIndex1], imagesPathArray[randomIndex2] = imagesPathArray[randomIndex2], imagesPathArray[randomIndex1]
        imagesLabelsArray[randomIndex1], imagesLabelsArray[randomIndex2] = imagesLabelsArray[randomIndex2], imagesLabelsArray[randomIndex1]
    return imagesPathArray, imagesLabelsArray

    
def getBatchOfLetterImages(batchSize=64):
    global startIndexOfBatch
    global imagesPathArray
    dataset = np.ndarray(shape=(0, 784), dtype=np.float32)
    labels = np.ndarray(shape=(0, 10), dtype=np.float32)
    with tf.Session() as sess:
        for i in range(startIndexOfBatch, len(imagesPathArray)):
            pathToImage = imagesLabelsArray[i]+imagesPathArray[i]
            lastIndexOfSlash = pathToImage.rfind("/")
            folder = pathToImage[lastIndexOfSlash - 1] 
            if(not pathToImage.endswith(".DS_Store")):
                try:
                    imageContents = tf.read_file(str(pathToImage))
                    image = tf.image.decode_png(imageContents, dtype=tf.uint8)
                    resized_image = tf.image.resize_images(image, [28, 28]) 
                    imarray = resized_image.eval()
                    imarray = imarray.reshape(784)
                    appendingImageArray = np.array([imarray], dtype=np.float32)
                    appendingNumberLabel = np.array([getNumber(folder)], dtype=np.float32)
                    labels = np.append(labels, appendingNumberLabel, axis=0)
                    dataset = np.append(dataset, appendingImageArray, axis=0)
                    if(len(labels) >= batchSize):
                        startIndexOfBatch = i+1
                        return labels, dataset
                except:
                    print("Unexpected Image, it's okay, skipping")
                    
startIndexOfBatch = 0
imagesPathArray, imagesLabelsArray = getListOfImages()
imagesPathArray, imagesLabelsArray = shuffleImagesPath(imagesPathArray, imagesLabelsArray)



tf.reset_default_graph()

x = tf.placeholder(tf.float32, shape=[None, 784])
W = tf.Variable(tf.truncated_normal([784, 10]), dtype=tf.float32, name="weights_0")
b = tf.Variable(tf.truncated_normal([10]), dtype=tf.float32, name="bias_0")
y = tf.nn.softmax(tf.matmul(x, W) + b)



trainingRate = 0.001
trainingLoops = 5
batchSize = 100

yTrained = tf.placeholder(tf.float32, [None, 10])

crossEntropy = -tf.reduce_sum(yTrained * tf.log(y))

trainStep = tf.train.GradientDescentOptimizer(trainingRate).minimize(crossEntropy)


saver = tf.train.Saver()
    
with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    for i in range(0, trainingLoops):
        print("Training Loop number: ", i)
        batchY, batchX = getBatchOfLetterImages(batchSize)
        print(batchX.shape, batchY.shape)
        session.run(trainStep, feed_dict={x: batchX, yTrained: batchY})

    saver = tf.train.Saver(write_version=tf.train.SaverDef.V1)
    savedPath = saver.save(session, "./model.ckpt")
    print("Model saved at: " ,savedPath)