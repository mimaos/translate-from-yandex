#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import request
import requests
import json
from io import StringIO

app = Flask(__name__)

@app.route('/translateenglish', methods=['GET'])
def translateenglish():
    if request.method == 'GET':
        text = request.args['textToTranslate']

        params = {
        'key':'trnsl.1.1.20190902T115551Z.906ad44dda89b9c9.7f34373544729af9424560734269a2f63f949a8f',
        'lang':'en-ru',
        'text':text
        }

        r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=params)

        io = StringIO(r.text)
        result = json.load(io)['text']
        return result[0]

