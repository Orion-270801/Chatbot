# Chatbot
Run train.py file to train the chatbot. Change the location of intents.json with new location.

Run app.py. It would generate the api.

Put that api in postman as a post request and input the json file in following format

Example format.

{"Name": "Mritunjoy Halder",

"Age":"20 yrs",

"Weight":"40Kg",

"Blood Pressure":"100",

"message":["No Fever","Cough Present","Dry Throat"]

}

It would generate the output as json.



Libraries Required to train and test the model.

nltk, version 3.5


tflearn, version 0.5.0

numpy 1.19.2

flask 1.1.2
