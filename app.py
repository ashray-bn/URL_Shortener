from flask import Flask, request, jsonify, redirect
import random
import requests

app=Flask(__name__)

url_store = {} #in memory storage

def generate_code(l=6): #generate a random code of length l
    code=""
    while True:
        for i in range (l):
            alornum=random.randint(0,1)
            code+=alornum*(str(random.randint(0,9)))+((1-alornum)*chr(random.randint(65,90)))
        if code not in url_store:
            return code

@app.route('/shorten',methods=['POST']) #accepts a POST request with a JSON body containing the original URL and an optional custom code
def shorten():
    data = request.get_json() #stores original url and custom code (if entered) in a dictionary
    original_url=data["url"]
    custom_code=data.get("custom_code") #evalutes to None if custom code is not provided

    if not original_url:
        return jsonify({"error":"Original URL is required"})

    if custom_code:
        if custom_code in url_store:
            return jsonify({"error":"Custom Code already exists"})
        code=custom_code
    else:
        code=generate_code()
    url_store[code]={"url":original_url,"clicks":0}

    return jsonify({"short_url":"http://127.0.0.1:5000/"+code,"original_url":original_url,"code":code})

@app.route('/<code>',methods=['GET']) #redirects to the original URL
def redirect_to_url(code):
    if code not in url_store:
        return jsonify({"error": "Short URL not found"}),404
    url_store[code]["clicks"] += 1

    return redirect(url_store[code]["url"], code=302)

@app.route("/stats/<code>", methods=["GET"]) #returns the statistics for a given short URL
def get_stats(code):
    if code not in url_store:
        return jsonify({"error": "Short URL not found"})

    return jsonify({"original_url": url_store[code]["url"],"short_code": code,"clicks": url_store[code]["clicks"]})
    
if __name__ == "__main__": #run the app
    app.run(debug=True)

'''
on bash to POST
curl -X POST http://127.0.0.1:5000/shorten \
-H "Content-Type: application/json" \
-d '{"url":"https://google.com", "custom_code":"myurl"}' google can we any url
'''
'''
response = requests.post("http://localhost:5000/shorten",json={"url": "https://google.com", "custom_code": "myurl"})
print(response.json())
'''