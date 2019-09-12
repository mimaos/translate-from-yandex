#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import request
import requests
import json
from io import StringIO

app = Flask(__name__)

@app.route('/translateenglish', methods=['POST'])
def translateenglish():
    if request.method == 'POST':
        data = request.get_json()
        text = data['text']
        print(text)
        params = {
        'key':'trnsl.1.1.20190902T115551Z.906ad44dda89b9c9.7f34373544729af9424560734269a2f63f949a8f',
        'lang':'en-ru',
        'text':text
        }
        
        r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params)

        io = StringIO(r.text)
        result_yandex = json.load(io)
        result_text = result_yandex['text']

        result = {
            'text':result_text
            }
       
        return result
