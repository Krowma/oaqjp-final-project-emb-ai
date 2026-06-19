import requests
import json

def emotion_detector(text_to_analyze):
    """analyse the text passed as parameter and return the associated emotion"""
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    myobj = { "raw_document": { "text": text_to_analyze } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json = myobj, headers=header)
    
    print(response.status_code)

    if(response.status_code == 400):
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None,}

    formatted_response = json.loads(response.text)
    emotions_result = formatted_response['emotionPredictions'][0]['emotion']

    highest_score = 0
    dominant_emotion = None
    for label, score in emotions_result.items():
        if(score > highest_score):
            dominant_emotion = label
            highest_score = score
    
    emotions_result['dominant_emotion'] = dominant_emotion
    return emotions_result

    

