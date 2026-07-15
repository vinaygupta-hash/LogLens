from flask import Flask, render_template, request, send_file, redirect
from config import *
from analyzer import counting
import csv
import os

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = SECRET_KEY

# Create uploads folder if it doesn't exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

last_uploaded_file = None


@app.route("/")
def home():
    return redirect("/upload")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    global last_uploaded_file

    result = None

    if request.method == "POST":

        # Check if file exists
        if "logfile" not in request.files:
            return render_template(
                "upload.html",
                result=None,
                error="❌ No file was uploaded."
            )

        file = request.files["logfile"]

        # Check if user selected a file
        if file.filename == "":
            return render_template(
                "upload.html",
                result=None,
                error="❌ Please choose a file."
            )

        # Allow only .log and .txt files
        allowed_extensions = {"log", "txt"}

        filename = file.filename

        if "." not in filename:
            return render_template(
                "upload.html",
                result=None,
                error="❌ Invalid file."
            )

        extension = filename.rsplit(".", 1)[1].lower()

        if extension not in allowed_extensions:
            return render_template(
                "upload.html",
                result=None,
                error="❌ Only .log and .txt files are supported."
            )

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        try:
            result = counting(file_path)
            last_uploaded_file = file_path

        except UnicodeDecodeError:
            return render_template(
                "upload.html",
                result=None,
                error="❌ Unable to read the file. Please upload a valid UTF-8 log file."
            )

        except Exception:
            return render_template(
                "upload.html",
                result=None,
                error="❌ Something went wrong while analyzing the file."
            )

    return render_template("upload.html", result=result)


@app.route("/download")
def download():

    if last_uploaded_file is None:
        return render_template(
            "upload.html",
            result=None,
            error="❌ Please upload and analyze a file first."
        )

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

    return send_file(
        "analysis_report.csv",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)