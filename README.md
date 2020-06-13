# TwitterHateSpeech
This repository is for hate speech detection in Twitter for a variety of domains like Religion, Race, etc.

Domain Adaptation for Hate Speech Detection using LSTMs

Twitter is a microblogging and social networking service on which users post and interact with messages known as "tweets".
It is a platform where you can easily share news from everywhere, making it an efficient medium for communication.

Hate speech is defined  as "public speech that expresses hate or encourages violence towards a person or group based on something such as race, religion, sex, or sexual orientation.

Hate speech detection involves the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information.

The data is collected using web crawling and stored as a CSV and as a pickled pandas dataframe (Python 2.7)
class labels: 0 - hate speech; 1 - non hate speech

This project makes use of tweepy; a python library used for accessing the Twitter API, and flask for deploying it as a web-application.

The tweepy library requires a functioning twitter developer account and an application on developer.twitter.com in order to generate consumer key, consumer key secret, access token and access token secret.
These values are used by tweepy to make twitter API request calls in order to receive the tweets that are analyzed.
This is how web crawling is done for tweets using a particular hashtag.

After you have successfully made an application, generate the 4 variables on the developer.twitter.com website.
consumer_key = 'your consumer key';
consumer_secret = 'your consumer secret key';
access_token = 'your access token';
access_token_secret = 'your access token secret';

Clone or download the repository and extract it into a folder and open it.

cd into the directory and run the application using the command:
python app.py

Install all the necessary packages required, which are (to state a few):
tweepy
flask
numpy

You can use the following pip command to download and install these libraries:
pip install moduleName

Open the localhost address (127.0.0.1:5000) and use the application to analyze any hashtag.
