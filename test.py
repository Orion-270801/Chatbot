import requests
from flask import Flask, render_template, request, jsonify
BASE = "http://0.0.0.0:5000/"
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def res():
	return render_template('index.html')
@app.route('/get',methods=['GET','POST'])
def getBotResponse():
	if request.method == 'POST':
		name = request.form.get('Name')
		age = request.form.get('Age')
		weight = request.form.get('Weight')
		BloodPressure = request.form.get('BP')		 
		message = request.form.getlist('mycheckbox')
		string = ""
		for i in message:
			string = string + i
		result = str('Name: '+name+'<br/>'+'Age: '+age+'<br/>'+'Weight: '+weight+'<br/>'+'Blood Pressure: '+BloodPressure+'<br/>'+'Ailments Noted: '+"message"+'<br/>'+'Analysis: '+"Analysis"+'<br/>')
	response = requests.get(BASE+"mj/"+string)
	print(response.json())
	return result
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5050)

