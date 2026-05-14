from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "Hllo, Jenkins CI/CD from Flask App on Windows!"


if __name__=="__main__":
    app.run(debug=True)