#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template_string, request
import requests
import json
import base64

app = Flask(__name__)

# HTML Template with CSS
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Predictive Maintenance</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('data:image/jpeg;base64,{{ background_image }}'); /* Set background image */
            background-size: cover; /* Cover the entire background */
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: rgba(255, 255, 255, 0.8); /* Semi-transparent background */
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
            padding: 20px;
            width: 800px; /* Width of the container */
            height: 600px; /* Height of the container */
            overflow-y: auto; /* Add a scrollbar if contents are long */
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .form-group {
            margin: 15px 0;
        }
        label {
            display: block;
            margin-bottom: 5px;
            color: #666;
        }
        input[type="text"] {
            width: calc(100% - 10px); /* Reduce input field width */
            padding: 10px;
            padding-right: 5px; /* Reduce padding from the right */
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #8B4513; /* Light brown color */
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        input[type="submit"]:hover {
            background-color: #704214; /* Darker brown on hover */
        }
        .result {
            margin-top: 20px;
            text-align: center;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Predictive Maintenance</h1>
        <form method="POST">
            <div class="form-group">
                <label for="Type">Type</label>
                <input type="text" id="Type" name="Type" required>
            </div>
            <div class="form-group">
                <label for="Air temperature [K]">Air temperature [K]</label>
                <input type="text" id="Air temperature [K]" name="Air temperature [K]" required>
            </div>
            <div class="form-group">
                <label for="Process temperature [K]">Process temperature [K]</label>
                <input type="text" id="Process temperature [K]" name="Process temperature [K]" required>
            </div>
            <div class="form-group">
                <label for="Rotational speed [rpm]">Rotational speed [rpm]</label>
                <input type="text" id="Rotational speed [rpm]" name="Rotational speed [rpm]" required>
            </div>
            <div class="form-group">
                <label for="Torque [Nm]">Torque [Nm]</label>
                <input type="text" id="Torque [Nm]" name="Torque [Nm]" required>
            </div>
            <div class="form-group">
                <label for="Tool wear [min]">Tool wear [min]</label>
                <input type="text" id="Tool wear [min]" name="Tool wear [min]" required>
            </div>
            <input type="submit" value="Get Prediction">
        </form>
        {% if prediction %}
            <div class="result">
                <h3>Prediction Result: {{ prediction }}</h3>
            </div>
        {% endif %}
    </div>
</body>
</html>
'''

def get_prediction(features):
    url = 'http://2b829f7a-0608-497a-8528-7dec86abe1c3.eastus.azurecontainer.io/score'  
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'data': features})
    response = requests.post(url, headers=headers, data=data)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        features = [
            request.form['Type'],
            request.form['Air temperature [K]'],
            request.form['Process temperature [K]'],
            request.form['Rotational speed [rpm]'],
            request.form['Torque [Nm]'],
            request.form['Tool wear [min]']
        ]
        prediction = get_prediction(features)

    # Read the image and convert it to base64
    with open('Engineer-operator-repairs-valve-equipment-in-plant-industry.jpg', 'rb') as img:
        background_image = base64.b64encode(img.read()).decode('utf-8')

    return render_template_string(html_template, prediction=prediction, background_image=background_image)

if __name__ == '__main__':
    try:
        app.run(port=5012, debug=True, use_reloader=False)
    except Exception as e:
        print(f"Error occurred: {e}")


# In[2]:


import urllib.request
import json
import os
import ssl
import tkinter as tk

def allowSelfSignedHttps(allowed):
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

def send_request():
    allowSelfSignedHttps(True)

    # Request data
    data = {
        "Inputs": {
            "input1": [
                {
                    "Path": "sample_path_1",  
                    "UDI": 1,
                    "Air temperature [K]": 298.1,  
                    "Process temperature [K]": 308.6,  
                    "Rotational speed [rpm]": 1551,  
                    "Torque [Nm]": 42.8,  
                    "Tool wear [min]": 0,  
                    "Target": 0,
                    "Failure Type": "No Failure",  
                    "Product ID": "M14860",  
                    "Type": "M"  
                },
                {
                    "Path": "sample_path_2", 
                    "UDI": 2,
                    "Air temperature [K]": 298.2,  
                    "Process temperature [K]": 308.7,  
                    "Rotational speed [rpm]": 1408,  
                    "Torque [Nm]": 46.3,  
                    "Tool wear [min]": 3,  
                    "Target": 0,
                    "Failure Type": "No Failure",  
                    "Product ID": "L47181",  
                    "Type": "L"  
                }
            ]
        }
    }

    body = str.encode(json.dumps(data))
    url = 'http://2b829f7a-0608-497a-8528-7dec86abe1c3.eastus.azurecontainer.io/score'
    api_key = 'VOGzGyV6EMHi4fZwtHXhQjwyhWAQPjxH'

    headers = {'Content-Type':'application/json', 'Authorization':('Bearer ' + api_key)}
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        # Convert the result to a pretty JSON format for better readability
        formatted_result = json.dumps(json.loads(result), indent=4)
        result_label.config(text=formatted_result)  # Display the formatted result in the label
    except urllib.error.HTTPError as error:
        result_label.config(text="Error: " + str(error.code))
        print("The request failed with status code: " + str(error.code))
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))

# إعداد واجهة المستخدم
root = tk.Tk()
root.title("API Request Interface")

send_button = tk.Button(root, text="Send Request", command=send_request)
send_button.pack()

result_label = tk.Label(root, text="", wraplength=400)
result_label.pack()

root.mainloop()

