import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

#use the open method to open the CSV file as read only
#using the with statement simplifies exception handling by encapsulating
#preparation and cleanup tasks. It will also automatically close the file
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    #Instanteate an empty list of laureates
    results = []
    #check if there is a surname, if not return an empty list
    if not request.args.get("surname"):
        return jsonify(results)

    search_string = request.args.get("surname").lower().strip()
    
    for laureate in laureates:
        if search_string in laureate["surname"].lower():
            results.append(laureate)

    return jsonify(results)

app.run(debug=True)
