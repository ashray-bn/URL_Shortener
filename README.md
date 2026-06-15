# URL_Shortener
Simple app built in Flask aimed at shortening a URL and providing basic information such as the number of clicks of the shortened URL

 Requirements
 -Python3
 -Flask

 Running the app- 
 python app.py
 => server is running on 127.0.0.1:5000

 Features
 - Post /shorten
 Reuires a request body JSON file {"original_url":"...","custom_code":"..."} where custom code is optional
 this feature can be tested using curl command on bash or by the optional python code commented at the end of the code base (requires requests to be installed) or by using POSTMAN

 - Get /code
 Redirects to the original url and updates the counter internally

 - Get /stats/code
Gives you the number of clicks of the particular shortened URL and other details

Limitations (future improvements)
- no persistent storage
- no validation of URLs
- no expiration date of links
- no user auth
- no verification of randomness of code generated (cross referencing with a dictionary)
