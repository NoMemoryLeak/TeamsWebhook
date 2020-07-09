#!/usr/bin/env python3
from flask import Flask
from flask import request
import os
import json
import requests

app = Flask(__name__)
newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
messageBody = {
     "@type": "MessageCard",
     "@context": "http://schema.org/extensions",
     "title": "Teams Webhook - Link to GitHub",
     "summary": "Created New Task",
     "sections": [
        {
       "activityTitle": "Python Launch WebHook",
       "activitySubtitle": "07/07/2020",
       "activityImage": 
"https://fr.wikipedia.org/wiki/H%C3%A9risson#/media/Fichier:2008_Hedgehog_1020932.jpg",
       "facts": [{
             "name": "Description",
             "value": "Incomming Webhook"
         }, {
             "name": "Who",
             "value": "Seb.Goa"
         }, {
             "name": "Status",
             "value": "Envoyer depuis Alpha Centauri"
         }]
        }]
}

teams_url = os.getenv('TEAMS')
@app.route('/', methods=['POST', 'GET'])
def trans():

     ce = request.get_json()
     print(ce.keys())
     messageBody['title'] = ce['title']

     r = requests.post(teams_url,data=json.dumps(messageBody),headers=newHeaders)
     if r.status_code == 200 :
         body = {"message":"sent to teams"}
         response = app.response_class(response=json.dumps(body),status=200,mimetype='application/json') 
         return response
     else :
         print("Erreur dans la requete post")
         return 0

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080)