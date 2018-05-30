from flask import Flask, jsonify, request


app = Flask(__name__)

class User():
	users = [
    {"name": "godwinwabwile"},
    {"name": "Mbithe"},
    {"name": "hinga"}]
	def __init__(self, name, emai, password):
		self.name=name
		self.email= email
		self.password=password


class User():
	@app.route('/signin', methods=['POST'])
	def signin():
		return jsonify({"name":user})

	@app.route('/signup', methods=['POST'])
	def signup():
		return jsonify({"":""})

if __name__=="__main__":
	app.run(debug=True)