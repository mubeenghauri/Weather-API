### Weater API for ManyChat Dynamic Content
### Hosted at weather-api-demo-jssol.herokuapp.com
### credits : mubeenghauri ghauri.mubeen@gmail.com

import flask
from flask import request, jsonify
import requests
import json

app = flask.Flask(__name__)
app.config["Debug"] = True

### add search query after q
#api_url = "https://api.apixu.com/v1/current.json?key={key}&q="

@app.route('/',methods=["GET"])
def home():
    return """ <h1> Welcome to Mubeen's Weather API </h1>
    <p> You are currently at home </p> """


@app.route('/api/weather', methods=["GET"])
def weather():
    if 'city' in request.args:
        city = str(request.args['city'])
    else:
        return "No Args supplied"

    ### register to get your key
    api_url = "https://api.apixu.com/v1/current.json?key={{key}}&q="+city
    print(api_url)
    weather_data = requests.get(api_url)
    
    jsoned = json.loads(weather_data.text)
    cityName = jsoned["location"]["name"]
    condition = jsoned["current"]["condition"]["text"]
    temprature = jsoned["current"]["temp_c"]

    response = {
  "version": "v2",
  "content": {
    "messages": [
      {
        "type": "text",
        "text": "The weather in "+str(cityName)+" is "+str(condition)+" with temprature of "+str(temprature),
      }
    ],
  }
}
    #print(type(jsoned))
    #print(jsoned["location"])
    return response

if __name__ == '__main__':
        import os  
        port = int(os.environ.get('PORT', 33507)) 
        app.run(host='0.0.0.0', port=port)    # Uncoment when pushing to heroku
        #app.run()                            # Uncoment when running locally