from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    r = emotion_detector(text_to_analyze)

    return f"For the given statement, the system response is 'anger': {r['anger']}, 'disgust': {r['disgust']}, 'fear': {r['fear']}, 'joy': {r['joy']}, 'sadness': {r['sadness']}. The dominant emotion is {r['dominant_emotion']}."

    
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)