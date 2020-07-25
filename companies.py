from flask import Flask, json, jsonify, request

companies = [
	{
		"id": 1,
		"name": "Sapient"
	},
	{
		"id": 2,
		"name": "GlobalLogic"
	},
	{
		"id": 3
	}
]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return 'Welcome to home page.\nCall individual APIs with right endpoint url.'

@app.route('/companies', methods=['GET'])
def get_companies():
	#return json.dumps(companies)
	return jsonify(companies)

@app.route('/companies', methods=['POST'])
def add_company():
	companies.append(request.get_json())
	return jsonify({'Success': True}), 201

if _name_ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)







