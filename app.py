from flask import Flask, render_template, request
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
	dat = request.get_json()
	game = dat["game"]
	if (db.data.find({"game": game}).count() == 0):
		print "no type shots"
		data = {}
		data["type"]="shots"
		data["data"]=[dat]
		data["game"] = game
		db.data.insert(data)
	else:
		print "update type shots"
		db.data.update({'game':game}, 
			{'$push': {"data": [dat]}})
	return "Submitted data"

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
