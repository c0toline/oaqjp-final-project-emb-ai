"""Module that would receibe a text input, then it would
use the Watson NLP library to process and return the 
preddiction of the emotions with a correct format
"""

import json
import requests as r

"""Function to receibe and process the text"""
def emotion_detector(text_to_analayze: str) -> dict:
    """It takes a text input from the user
        and return a formated JSON dictionary
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analayze
        }
    }

    response = r.post(
        url,
        headers=headers,
        json=input_json
    )

    formated_response = json.loads(response.text)

    emotions = formated_response["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(emotions, key=emotions.get)

    formatted_emotions = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }

    return formatted_emotions