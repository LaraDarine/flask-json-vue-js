#!flask/bin/python
from os import abort

from flask import Flask, jsonify, request, json, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    # Create an empty list
    data = []
    # open the json file
    with open('./data.json', 'r') as jsonfile:
            data.append(json.load(jsonfile))
    
    if request.method == "POST":
        # get new data from the html form element
        name = request.form['name']
        model = request.form['model']
        new_data = {
            'name': name,
            'model': model
        }
        # add it to the list
        data.append(new_data)
        # write the updates to the json file
        with open('./data.json', 'w') as outjsonfile:
            json.dump(data, outjsonfile)
        return render_template('add_article.html', data=data)
        

    if request.method == "GET":
        return render_template('add_article.html', data=data)


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