from flask import Flask, render_template, request
from JSONEncoder import JSONEncoder
import os
import server

app = Flask(__name__)
db = server.get_db()

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/options")
def main():
	return render_template("options.htm.j2")

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

@app.route("/addOptions", methods = ["POST"])
def add_options():
	dat = request.get_json()
	dat_type = dat["type"]
	if (db.options.find({"type":dat_type}).count()==0):
		data = {}
		data["type"]="game"
		data["data"] = [dat]
		db.options.insert(dat)
	else:
		db.options.update({"type":dat_type},
			{'$push':{"data":[dat]}})
	return "Added options"

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
