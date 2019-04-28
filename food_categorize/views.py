# -*- coding: utf-8 -*-
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from konlpy.tag import Twitter
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import json

# def get_noun(text):
#     nouns = tokenizer.nouns(text)
#     return [n for n in nouns]
# tokenizer = Twitter()
food_model = joblib.load(os.getcwd()+'/food_categorize/food_categorize_model.pkl')


# Create your views here.
@csrf_exempt
def predict(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    received_json_data = received_json_data['content']
    result = food_model.predict([received_json_data])
    json_obj = {'category': result[0]}
    return HttpResponse(
        json.dumps(json_obj),
        content_type = 'application/javascript; charset=utf8'
    )
