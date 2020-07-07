#!/usr/bin/env python3.8
#This is a simple python script to monitor web pages

from flask import Flask, request, render_template, url_for
import requests
from socket import gaierror, gethostbyname

from werkzeug.utils import redirect

app = Flask(__name__)

app = Flask(__name__)

@app.route('/')
def search():
    return render_template('dynamic_input.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method == 'GET':
        return redirect(url_for('search'))
    else:
        status=[]
        input_values = request.form.getlist('input_text[]')
        checkbox_values = request.form.getlist('input_checkbox')
        print(type(input_values))
        for i in input_values:
            response = requests.get(i, timeout=1.00)
            if response.status_code is 200:
                status.append(i)
            else:
                print (f'the site {i} is down')
        return render_template('dynamic_input_results.html',
                               input_values = input_values,
                               checkbox_values = checkbox_values,
                               status = status)



if __name__ == '__main__':
    app.run(debug=False, port=5001)