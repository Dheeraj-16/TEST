import pyrebase

config = {
    "apiKey": "AIzaSyCQZNQt2Mx9JI2EpBpmPrnZXKPJV57FgMY",
    "authDomain": "test-c8298.firebaseapp.com",
    "databaseURL": "https://test-c8298.firebaseio.com",
    "projectId": "test-c8298",
    "storageBucket": "test-c8298.appspot.com",
    "messagingSenderId": "113078646908",
    "appId": "1:113078646908:web:1f76d67ec58df8ab6331f9",
    "measurementId": "G-QEGBC5HJ2K"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add':

			name = request.form['name']
			db.child("todo").push(name)
			todo = db.child("todo").get()
			to = todo.val()
			return render_template('index.html', t=to.values())
		elif request.form['submit'] == 'delete':
			db.child("todo").remove()
		return render_template('index.html')
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)