# 🔍 LogLens

> **A modern Flask-based log analysis dashboard that extracts meaningful insights from server log files.**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![HTML5](https://img.shields.io/badge/HTML5-orange?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-blue?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-yellow?style=for-the-badge&logo=javascript)

</p>

---

## 📖 About

LogLens is a web-based log analysis application built with **Python** and **Flask**.

Instead of manually searching through hundreds of log entries, users can upload a log file and instantly receive a summarized dashboard containing:

- Log level statistics
- Unique IP addresses
- Timestamps
- Exception types
- CSV export

The project demonstrates practical backend development, file processing, regular expressions, data structures, and a clean responsive user interface.

---

# ✨ Features

- 📂 Upload log files
- 📊 Detect log levels
    - INFO
    - WARNING
    - ERROR
    - DEBUG
    - CRITICAL
- 🌐 Extract unique IP addresses
- 🕒 Extract timestamps
- ⚠ Detect exception types using Regex
- 📈 Analysis Summary Dashboard
- 📄 Export results as CSV
- 🎨 Modern Responsive UI
- ⚡ Fast line-by-line log parsing

---

# 📸 Screenshots

> Screenshots will be added after deployment.

### Home

*(Add screenshot here)*

---

### Dashboard

*(Add screenshot here)*

---

### CSV Report

*(Add screenshot here)*

---

# 🛠 Tech Stack

### Backend

- Python
- Flask

### Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2

---

# 🧠 Python Concepts Used

- File Handling
- Dictionaries
- Lists
- Sets
- Regular Expressions (Regex)
- CSV Module
- Exception Handling
- Functions
- Loops

---

# 📂 Project Structure

```text
LogLens/

│

├── static/
│   └── css/
│       └── style.css

├── templates/
│   └── upload.html

├── uploads/

├── analyzer.py
├── app.py
├── config.py

├── requirements.txt

├── .gitignore

└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/vinaygupta-hash/LogLens.git
```

Go inside the project

```bash
cd LogLens
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000/upload
```

---

# 📊 What LogLens Analyzes

✅ Log Level Statistics

✅ Total Log Entries

✅ Unique IP Addresses

✅ Timestamps

✅ Exception Types

✅ CSV Report

---

# 📄 Sample CSV Output

| Log Level | Count |
|-----------|------:|
| INFO | 25 |
| WARNING | 7 |
| ERROR | 5 |
| DEBUG | 11 |
| CRITICAL | 2 |

---

# 💡 Why I Built This Project

I built LogLens to strengthen my backend development skills with Flask while learning how real-world log analyzers work.

The project focuses on efficient log parsing, extracting meaningful information using Regular Expressions, and presenting the results through a clean dashboard instead of raw terminal output.

---

# 🔮 Future Improvements

- Multiple log file upload
- Advanced search & filtering
- Interactive charts
- PDF report generation
- Docker support
- REST API
- Support for Apache/Nginx log formats

---

# 🌐 Live Demo

🚀 Coming Soon (Render Deployment)

---

# 👨‍💻 Author

### Vinay Gupta

🎓 B.Tech Computer Science Engineering

💻 Python Backend Developer (Learning)

🔗 GitHub:
https://github.com/vinaygupta-hash

🔗 LinkedIn:
https://www.linkedin.com/in/vinay-gupta-31966837b

---

# ⭐ If you like this project

If you found this project helpful, consider giving it a ⭐ on GitHub.

It motivates me to build more useful open-source projects.

---

<p align="center">

Made with ❤️ using Flask & Python

</p>