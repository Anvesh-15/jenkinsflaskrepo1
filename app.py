from flask import Flask
app=Flask(_name_)

@app.route("/")
def home():
    return "HEllo, Jenkins CI/CD from Flask App on Windows!"


if _name_=="_main_":
    app.run(debug=True)