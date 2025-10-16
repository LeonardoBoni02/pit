
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

'''
Nota : potrebbe essere necessario costruire un file di requirements in python ( google it!)

Explanation
Import Flask: The Flask class is imported from the flask package.
Create an Instance: An instance of the Flask class is created.
Define a Route: A route is defined using the @app.route('/') decorator, which maps the URL to the hello_world function.
Return Statement: The hello_world function returns the string "Hello, World!" when accessed.
Run the Application: The app runs in debug mode, which is useful during development to catch errors.
Running the Flask App
Make sure you have Flask installed. You can install it using pip:
bash

Copia codice
pip install Flask
Save the code in a file named app.py.
Run the file:
bash

Copia codice
python app.py
Open a web browser and go to http://127.0.0.1:5000 to see the message "Hello, World!".
'''