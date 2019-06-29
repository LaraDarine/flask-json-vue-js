#!flask/bin/python
from os import abort

from flask import Flask, jsonify, request, json, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    # Additionally, we're now loading the JSON file's data into file_data
    # every time a request is made to this endpoint
    if request.method == "POST":
        data = request.json
        print(data)

    if request.method == "GET":
        return render_template('add_article.html')


    '''
    with open('./data.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
        data1=file_data
    data1['name'] = "bmw"

    with open('./data.json', 'w') as jsonfile:
        json.dump(data1,jsonfile)
    # We can then find the data for the requested date and send it back as json
    return json.dumps(file_data['name'])
    '''


if __name__ == '__main__':
    app.run(debug=True)