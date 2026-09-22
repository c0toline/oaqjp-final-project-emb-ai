"""Flask server for the Emotion Detection web application"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the text provieded by the user ande return emotions results"""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the main page of the Emotion Detection application."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    