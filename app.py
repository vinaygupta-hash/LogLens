from flask import Flask, render_template, request, send_file, redirect
from config import *
from analyzer import counting
import csv, os

app=Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = SECRET_KEY

last_uploaded_file= None


@app.route("/")
def home():
    return redirect("/upload")

@app.route("/upload",methods=["GET","POST"])
def upload():
    global last_uploaded_file
    result= None
    if request.method=="POST":
        if "logfile" not in request.files:
            return "No file uploaded."

        file = request.files["logfile"]
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)
        
        result= counting(file_path)
        print(result)
        
        last_uploaded_file = file_path
    return render_template("upload.html",result=result)


@app.route("/download")
def download():

    if last_uploaded_file is None:
        return "Please upload a file first."

    result = counting(last_uploaded_file)

    with open("analysis_report.csv", "w", newline="") as f:
        writer = csv.writer(f)

        # Log Counts
        writer.writerow(["Log Level", "Count"])
        for level, count in result["log_counts"].items():
            writer.writerow([level, count])

        writer.writerow([])

        # IP Addresses
        writer.writerow(["IP Addresses"])
        for ip in result["ip_addresses"]:
            writer.writerow([ip])

        writer.writerow([])

        # Exception Types
        writer.writerow(["Exception Types"])
        for exception in result["exceptions"]:
            writer.writerow([exception])

        writer.writerow([])

        # Timestamps
        writer.writerow(["Timestamps"])
        for timestamp in result["timestamps"]:
            writer.writerow([timestamp])

    return send_file("analysis_report.csv", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
    