'''
    This code imports Flask rending_template and request from flask package
    also imports emotion_detector from custom package
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiates Flask
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def send_emotion():
    '''
        This code analyzes the text sent from POST request
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    r = emotion_detector(text_to_analyze)

    # Error handle to check if dominant emotion is None
    if r['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is
    'anger': {r['anger']}, 'disgust': {r['disgust']}, 'fear': {r['fear']}, 'joy': {r['joy']}, 'sadness': {r['sadness']}. 
    The dominant emotion is {r['dominant_emotion']}."""


@app.route("/")
def index():
    ''' 
        This code renders index.html
    '''
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
