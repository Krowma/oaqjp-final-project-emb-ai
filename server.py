"""Route manage for Emotion Detector app with Flask"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    """Request text analysis and return formatted result"""
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_text = "For the given statement, the system response is "
    response_text +=  '\'anger\': ' + str(result['anger']) + ", "
    response_text +=  '\'disgust\': ' + str(result['disgust']) + ", "
    response_text +=  '\'fear\': ' + str(result['fear']) + ", "
    response_text +=  '\'joy\': ' + str(result['joy']) + ", "
    response_text +=  '\'sadness\': ' + str(result['sadness']) + ". "
    response_text += "The dominant emotion is " + result['dominant_emotion'] + "."

    return response_text


@app.route("/")
def render_index_page():
    """return main html template"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
