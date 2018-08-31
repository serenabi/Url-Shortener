# imports
from flask import Flask, request, render_template, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

from urllib.parse import urlparse
from urllib.request import urlopen

import string, os

# hosted on Heroku platform
host_url = 'https://z-urlshortener.herokuapp.com/'

# flask app and database
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Url(db.Model):
	__tablename__ = 'url'
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(1000))	

	def __init__(self, url):
		self.url = url		

	def __repr__(self):
		return 'Url: %s' % (self.url)

# Base36 Encodings
def toBase36(num):
	'''
	Function that takes in a number and returns base36 encoding	
	'''	
	chars = string.digits + string.ascii_lowercase
	encoded = ''
	while num > 0:
		num, remainder = divmod(num, 36)
		encoded = chars[remainder] + encoded
	return encoded

# Base36 Decodings
def toBase10(encodedString):
	'''
	Function that takes in a base36 encoding and returns decoded number
	'''
	decoded = int(encodedString, 36)
	return decoded

# View 01 - for Web Service
@app.route('/shorten_url', methods=['POST'])
def post():
	url_json = request.get_json()
	url_original = url_json['url']
	if urlparse(url_original).scheme == '':
			url_original = 'http://' + url_original

	try:
		urlopen(url_original)

		url = Url(url_original)
		db.session.add(url)
		db.session.commit()

		url_id = url.id
		encoded_string = toBase36(url_id)
		short_url = host_url + encoded_string

		return jsonify({'shortened_url': short_url})
	except:
		return "The URL doesn't seem to work. Please check."

# View 02 - for Web Service
@app.route('/<short_url>', methods=['GET'])
def get(short_url):
	decoded_rowNum = toBase10(short_url)
	redirect_url = Url.query.filter_by(id=decoded_rowNum).first().url	
	return redirect(redirect_url)

# View - for Web Interface
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		url_original = request.form.get('url')
		if urlparse(url_original).scheme == '':
			url_original = 'http://' + url_original

		url = Url(url_original)
		db.session.add(url)
		db.session.commit()

		url_id = url.id
		encoded_string = toBase36(url_id)
		short_url = host_url + encoded_string
		
		return render_template('home.html', short_url = short_url, url=url_original)
		
	return render_template('home.html')

if __name__ == '__main__':	
	app.run(host='0.0.0.0', port=5000)
