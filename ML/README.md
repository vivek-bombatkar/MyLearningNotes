###

## 1. ML kick start course  
> https://medium.com/open-machine-learning-course/open-machine-learning-course-topic-1-exploratory-data-analysis-with-pandas-de57880f1a68
- Exploratory Data Analysis with Pandas
- Visual Data Analysis with Python
- Classification, Decision Trees and k Nearest Neighbors
- Linear Classification and Regression
- Bagging and Random Forest
- Feature Engineering and Feature Selection
- Unsupervised Learning: Principal Component Analysis and Clustering
- Vowpal Wabbit: Fast Learning with Gigabytes of Data
- Time Series Analysis with Python, Predicting the future with Facebook Prophet
- Gradient Boosting


## 2. Google TF kick start
> https://developers.google.com/machine-learning/crash-course/~~
> https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=rTX3heEtu0b2

## 3. Random Notes
> http://queirozf.com/entries/matplotlib-pylab-pyplot-etc-what-s-the-different-between-these

### 3.1 Finding text from image.
> https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/cloud-client/detect/detect.py
> https://cloud.google.com/vision/docs/detecting-text#vision-text-detection-python
> https://github.com/GoogleCloudPlatform/cloud-vision/tree/master/python/text

```
$ detect.py text C:\Users\vkbomb\Downloads\award.JPG

Texts:

"bla bla bla"
```

> https://docs.aws.amazon.com/rekognition/latest/dg/text-detecting-text-procedure.html

> https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-print-text


### 3.2 chatboats for slack
> https://www.analyticsvidhya.com/blog/2018/03/how-to-build-an-intelligent-chatbot-for-slack-using-dialogflow-api/
> https://github.com/mohdsanadzakirizvi/Slack-AI-ChatBot

```
- Creating sample Slack Workspace
- Creating sample Boat Slack Application
- Get OAuth & Permissions from slack
- Export vars for Slack to code handshake
$export SLACK_TOKEN=<your_bot_user_oauth_token_here>
$export BOTNAME=<your_botname_here>
- execute the code 
```


> https://blog.algorithmia.com/sentiment-analysis-slack-chatbot-python/



## Common Issues

### No module named 'google.cloud'
- Cant locate google.cloud in pyCharm Package list
> https://github.com/GoogleCloudPlatform/google-cloud-python/issues/2366

```
#From Terminal 
pip install google-cloud
pip install --upgrade google-cloud
```


