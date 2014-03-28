import os 

from flask import Flask, jsonify, json, request, abort

app = Flask(__name__)

Calender_list = [

		{'CalId':1,'Entries':[]},

		{'CalId':2,'Entries':[{'ID':1,'Date':'23/10/2013','Description':'Swim Training','Start':'9.00','End':'10.00','Repeats':'none','Location':'www.location.com'},

		]}]
@app.route('/Assignment/<int:ID>', methods = ['POST'])
def Create_myCalender(ID):
	Calender_list.append({'CalId':ID,'Entries':[]})
	return "working\n"		
	

@app.route('/Assignment', methods = ['GET'])
def Get_Calender():
	return jsonify({'Calender_list':Calender_list})

@app.route('/Assignment/<int:CalId>', methods = ['GET'])
def Get_individual_Calender(CalId):
	for c in Calender_list:
		if c['CalId'] == CalId:
			return jsonify( {'Calender_list': Calender_list[0] } )
		return "No existing calender"

@app.route('/Assignment/<int:CalId>', methods = ['DELETE'])
def Delete_Calender(CalId):
	for c in Calender_list:
		if c['CalId'] == CalId:
			c.clear()
			Calender_list.remove({})
			return "calender deleted" 
		return "no such calender"

@app.route('/Assignment/<int:CalId>/<int:Entry_Id>', methods = ['POST'])
def create_CalEntry(CalId,Entry_Id):
	if not request.json or not 'Date'in request.json:
		abort(400)
	new_entry = {
		'ID': Entry_Id,
		'Date': request.json['Date'],
		'Description': request.json.get('Description',""),
		'Start': request.json.get('Start',""),
		'End': request.json.get('End',""),
		'Repeats': request.json.get('Repeats',""),
		'Location': request.json.get('Location',"")
	}
	for c in Calender_list:
		if c['CalId'] == CalId:
			for e in c['Entries']:
				if e == {}:
					c['Entries'].remove({})
					c['Entries'].append(new_entry)
					return "entry created"
				if e['ID']==Entry_Id:
					return "id is there"
			c['Entries'].append(new_entry)
			return "Entry created"
		return "Calender does not exist" 

if __name__=='__main__':
	app.run(debug = True)
