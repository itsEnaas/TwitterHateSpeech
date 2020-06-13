import os
from flask import Flask, render_template, request
from flask import send_from_directory
from classifier import *
import numpy as np

app = Flask(__name__)

hashtags_file_path = 'uploads/hashtags_searched.txt'

# home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST', 'GET'])
def analyzeTweet():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        hashtag = request.form['hashtag']
        f = open(hashtags_file_path, 'a')
        if hashtag:
            df = pd.read_csv('trump_tweets.csv')
            trump_tweets = df.Text
            trump_tweets = [x for x in trump_tweets if type(x) == str]
            trump_predictions = get_tweets_predictions(trump_tweets)

            print("Printing predicted values: ")
            for i, t in enumerate(trump_tweets):
                print(t)
                print(class_to_name(trump_predictions[i]))

            print("Calculate accuracy on labeled data")
            df = pd.read_csv('labeled_data.csv')
            tweets = df['tweet'].values
            tweets = [x for x in tweets if type(x) == str]
            tweets_class = df['class'].values
            predictions = get_tweets_predictions(tweets)
            right_count = 0

            for i, t in enumerate(tweets):
                if tweets_class[i] == predictions[i]:
                    right_count += 1

            accuracy = right_count / float(len(df))*100
            accuracy = round(accuracy)
            print("accuracy", accuracy)

            if accuracy > 0:
                return render_template('analyze.html', accuracy=accuracy, hashtag=hashtag)
            else:
                return render_template('analyze.html', error_message='No tweets found!')
        else:
            return render_template('analyze.html', error_message="Enter some hashtag!")

if __name__ == '__main__':
    app.run(debug=False, threaded=False)