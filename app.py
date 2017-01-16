from flask import Flask, render_template
from JSONEncoder import JSONEncoder
import os
import server

app = Flask(__name__)
db = server.get_db()

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/submit",methods = ["POST"])
def logData():
	print request.get_json()
	if (db.data.find({"type": "shots"}).count() == 0):
		print "no type shots"
		data = {}
		data["type"]="shots"
		data["data"]=[request.get_json()]
		db.data.insert(data)
	else:
		print "update type shots"
		db.data.update({'type':"shots"}, 
			{'$push': {"data": [request.get_json()]}})
	return "Submitted data"

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
