import requests
import json

#url = "enter heroku web app url here"
url = "https://nd0821-c3-starter-code-6-vhan.onrender.com/inference"


# explicit the sample to perform inference on
sample =  { 'age':40,
            'workclass':"Private", 
            'fnlgt':234721,
            'education':"Doctorate",
            'education_num':16,
            'marital_status':"Separated",
            'occupation':"Exec-managerial",
            'relationship':"Not-in-family",
            'race':"Black",
            'sex':"Female",
            'capital_gain':0,
            'capital_loss':0,
            'hours_per_week':30,
            'native_country':"Canada"
            }

data = json.dumps(sample)

# post to API and collect response
response = requests.post(url, data=data )

# display output - response will show sample details + model prediction added
print("response status code", response.status_code)
print("response content:")
print(response.json())